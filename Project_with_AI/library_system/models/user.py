import hashlib
from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    id: str
    name: str
    email: str
    password_hash: str
    role: str = "student"          # "student" | "admin"
    borrowed_book_ids: List[str] = field(default_factory=list)
    is_active: bool = True

    # ── password helpers ──────────────────────────────────────────
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == self.hash_password(password)

    # ── borrow / return ───────────────────────────────────────────
    def borrow_book(self, book_id: str) -> bool:
        if book_id in self.borrowed_book_ids:
            return False
        self.borrowed_book_ids.append(book_id)
        return True

    def return_book(self, book_id: str) -> bool:
        if book_id not in self.borrowed_book_ids:
            return False
        self.borrowed_book_ids.remove(book_id)
        return True

    # ── serialisation ─────────────────────────────────────────────
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "role": self.role,
            "borrowed_book_ids": self.borrowed_book_ids,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            password_hash=data["password_hash"],
            role=data.get("role", "student"),
            borrowed_book_ids=data.get("borrowed_book_ids", []),
            is_active=data.get("is_active", True),
        )

    def __str__(self) -> str:
        role_icon = "👑" if self.role == "admin" else "🎓"
        books = len(self.borrowed_book_ids)
        return (
            f"{role_icon} [{self.id}] {self.name} <{self.email}> "
            f"| Role: {self.role} | Borrowed: {books} book(s)"
        )
