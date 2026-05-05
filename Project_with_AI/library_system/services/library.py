import uuid
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

from models.book import Book
from models.transaction import Transaction, GRACE_DAYS
from models.user import User
from utils.file_handler import load_json, save_json


class Library:
    """Central service — manages books, users, transactions."""

    # ── init / persistence ────────────────────────────────────────
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.transactions: Dict[str, Transaction] = {}
        self._load_all()

    def _load_all(self):
        for d in load_json("books.json"):
            b = Book.from_dict(d)
            self.books[b.id] = b
        for d in load_json("users.json"):
            u = User.from_dict(d)
            self.users[u.id] = u
        for d in load_json("transactions.json"):
            t = Transaction.from_dict(d)
            self.transactions[t.id] = t

    def save_all(self):
        save_json("books.json",        [b.to_dict() for b in self.books.values()])
        save_json("users.json",        [u.to_dict() for u in self.users.values()])
        save_json("transactions.json", [t.to_dict() for t in self.transactions.values()])

    # ── helpers ───────────────────────────────────────────────────
    @staticmethod
    def _uid() -> str:
        return str(uuid.uuid4())[:8].upper()

    # ── book management ───────────────────────────────────────────
    def add_book(self, title: str, author: str, genre: str, quantity: int) -> Book:
        book = Book(
            id=f"B{self._uid()}",
            title=title.strip(),
            author=author.strip(),
            genre=genre.strip() or "General",
            quantity=quantity,
            available=quantity,
        )
        self.books[book.id] = book
        self.save_all()
        return book

    def remove_book(self, book_id: str) -> Tuple[bool, str]:
        if book_id not in self.books:
            return False, "Book not found."
        active = [t for t in self.transactions.values()
                  if t.book_id == book_id and t.status == "active"]
        if active:
            return False, f"Cannot remove — {len(active)} active issue(s) exist."
        del self.books[book_id]
        self.save_all()
        return True, "Book removed successfully."

    def update_book(self, book_id: str, **kwargs) -> Tuple[bool, str]:
        if book_id not in self.books:
            return False, "Book not found."
        book = self.books[book_id]
        for key, val in kwargs.items():
            if hasattr(book, key) and val is not None:
                setattr(book, key, val)
        self.save_all()
        return True, "Book updated."

    def get_all_books(self) -> List[Book]:
        return sorted(self.books.values(), key=lambda b: b.title.lower())

    def search_books(self, query: str) -> List[Book]:
        q = query.lower()
        return [
            b for b in self.books.values()
            if q in b.title.lower() or q in b.author.lower() or q in b.genre.lower()
        ]

    # ── user management ───────────────────────────────────────────
    def register_user(self, name: str, email: str, password: str,
                      role: str = "student") -> Tuple[bool, str, Optional[User]]:
        if any(u.email == email for u in self.users.values()):
            return False, "Email already registered.", None
        user = User(
            id=f"U{self._uid()}",
            name=name.strip(),
            email=email.strip().lower(),
            password_hash=User.hash_password(password),
            role=role,
        )
        self.users[user.id] = user
        self.save_all()
        return True, "User registered.", user

    def authenticate(self, email: str, password: str) -> Optional[User]:
        email = email.strip().lower()
        for user in self.users.values():
            if user.email == email and user.check_password(password):
                return user
        return None

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def delete_user(self, user_id: str) -> Tuple[bool, str]:
        if user_id not in self.users:
            return False, "User not found."
        user = self.users[user_id]
        if user.borrowed_book_ids:
            return False, "User has unreturned books."
        del self.users[user_id]
        self.save_all()
        return True, "User deleted."

    def get_all_users(self) -> List[User]:
        return sorted(self.users.values(), key=lambda u: u.name.lower())

    # ── issue / return ────────────────────────────────────────────
    def issue_book(self, book_id: str, user_id: str) -> Tuple[bool, str, Optional[Transaction]]:
        book = self.books.get(book_id)
        if not book:
            return False, "Book not found.", None
        if not book.is_available():
            return False, "Book not available (out of stock).", None

        user = self.users.get(user_id)
        if not user:
            return False, "User not found.", None
        if not user.is_active:
            return False, "User account is inactive.", None
        if book_id in user.borrowed_book_ids:
            return False, "User already has this book.", None

        today = date.today()
        txn = Transaction(
            id=f"T{self._uid()}",
            book_id=book_id,
            user_id=user_id,
            issue_date=today.isoformat(),
            due_date=(today + timedelta(days=GRACE_DAYS)).isoformat(),
        )
        book.update_stock(-1)
        user.borrow_book(book_id)
        self.transactions[txn.id] = txn
        self.save_all()
        return True, "Book issued successfully.", txn

    def return_book(self, book_id: str, user_id: str) -> Tuple[bool, str, float]:
        # Find active transaction
        txn = next(
            (t for t in self.transactions.values()
             if t.book_id == book_id and t.user_id == user_id and t.status == "active"),
            None,
        )
        if not txn:
            return False, "No active issue found for this book/user.", 0.0

        book = self.books[book_id]
        user = self.users[user_id]

        fine = txn.close()
        book.update_stock(+1)
        user.return_book(book_id)
        self.save_all()

        msg = f"Book returned. Fine: ৳{fine:.2f}" if fine else "Book returned. No fine 🎉"
        return True, msg, fine

    # ── transaction queries ───────────────────────────────────────
    def get_transactions(self, user_id: Optional[str] = None,
                         status: Optional[str] = None) -> List[Transaction]:
        txns = list(self.transactions.values())
        if user_id:
            txns = [t for t in txns if t.user_id == user_id]
        if status:
            txns = [t for t in txns if t.status == status]
        return sorted(txns, key=lambda t: t.issue_date, reverse=True)

    def get_overdue_transactions(self) -> List[Transaction]:
        today = date.today()
        return [
            t for t in self.transactions.values()
            if t.status == "active" and date.fromisoformat(t.due_date) < today
        ]

    # ── report ────────────────────────────────────────────────────
    def summary(self) -> dict:
        total_books = sum(b.quantity for b in self.books.values())
        available_books = sum(b.available for b in self.books.values())
        overdue = self.get_overdue_transactions()
        total_fine_collected = sum(
            t.fine for t in self.transactions.values() if t.status == "returned"
        )
        pending_fine = sum(t.calculate_fine() for t in overdue)
        return {
            "total_titles": len(self.books),
            "total_copies": total_books,
            "available_copies": available_books,
            "total_users": len(self.users),
            "active_issues": len([t for t in self.transactions.values() if t.status == "active"]),
            "overdue_count": len(overdue),
            "fine_collected": total_fine_collected,
            "fine_pending": pending_fine,
        }
