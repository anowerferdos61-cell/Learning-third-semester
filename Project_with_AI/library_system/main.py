"""
╔══════════════════════════════════════════════════════╗
║         📚  LIBRARY MANAGEMENT SYSTEM  📚           ║
║              CLI Edition — Python OOP                ║
╚══════════════════════════════════════════════════════╝
"""

import os
import sys

# ── path fix so imports work from any cwd ────────────────────────
sys.path.insert(0, os.path.dirname(__file__))

from services.library import Library
from models.user import User

# ─────────────────────────────────────────────────────────────────
#  UI helpers
# ─────────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BLUE   = "\033[94m"
GREY   = "\033[90m"

def clr(text, color): return f"{color}{text}{RESET}"
def ok(msg):    print(clr(f"  ✅  {msg}", GREEN))
def err(msg):   print(clr(f"  ❌  {msg}", RED))
def warn(msg):  print(clr(f"  ⚠️   {msg}", YELLOW))
def info(msg):  print(clr(f"  ℹ️   {msg}", CYAN))
def header(title):
    w = 54
    print(clr("═" * w, BLUE))
    print(clr(f"  {title}", BOLD + BLUE))
    print(clr("═" * w, BLUE))

def pause():
    input(clr("\n  Press Enter to continue...", GREY))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def prompt(label: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    val = input(clr(f"  → {label}{hint}: ", CYAN)).strip()
    return val if val else default

def prompt_int(label: str, min_val: int = 1) -> int:
    while True:
        try:
            val = int(prompt(label))
            if val < min_val:
                raise ValueError
            return val
        except ValueError:
            err(f"Please enter a valid number (≥ {min_val}).")

def pick(options: list, label: str = "Choose") -> str:
    for i, opt in enumerate(options, 1):
        print(clr(f"  {i}. {opt}", CYAN))
    while True:
        try:
            idx = int(prompt(label)) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            pass
        err("Invalid choice.")


# ─────────────────────────────────────────────────────────────────
#  Boot & login
# ─────────────────────────────────────────────────────────────────

def seed_demo_data(lib: Library):
    """Populate empty library with sample data."""
    if lib.books or lib.users:
        return
    info("Seeding demo data…")
    books = [
        ("Physical Chemistry", "P.W. Atkins", "Chemistry", 4),
        ("Introduction to Algorithms", "Cormen et al.", "Computer Science", 3),
        ("Clean Code", "Robert C. Martin", "Software Engineering", 5),
        ("The Pragmatic Programmer", "Hunt & Thomas", "Software Engineering", 2),
        ("Organic Chemistry", "Paula Bruice", "Chemistry", 3),
        ("Data Structures in Python", "Goodrich & Tamassia", "Computer Science", 4),
    ]
    for title, author, genre, qty in books:
        lib.add_book(title, author, genre, qty)

    # default admin
    lib.register_user("Admin", "admin@lib.com", "admin123", role="admin")
    lib.register_user("Anower Hossain", "anower@uni.com", "pass123", role="student")
    ok("Demo data loaded. Admin → admin@lib.com / admin123")


def login_screen(lib: Library) -> User:
    while True:
        clear()
        header("🔐  LOGIN")
        email    = prompt("Email")
        password = input(clr("  → Password: ", CYAN))
        user = lib.authenticate(email, password)
        if user:
            ok(f"Welcome, {user.name}! ({user.role})")
            pause()
            return user
        err("Invalid credentials. Try again.")
        pause()


# ─────────────────────────────────────────────────────────────────
#  Book menus
# ─────────────────────────────────────────────────────────────────

def menu_view_books(lib: Library):
    clear(); header("📚  ALL BOOKS")
    books = lib.get_all_books()
    if not books:
        warn("No books in library."); pause(); return
    for b in books:
        color = GREEN if b.is_available() else RED
        print(clr(f"  {b}", color))
    info(f"Total titles: {len(books)}")
    pause()

def menu_search_books(lib: Library):
    clear(); header("🔍  SEARCH BOOKS")
    query = prompt("Search (title / author / genre)")
    if not query:
        return
    results = lib.search_books(query)
    if not results:
        warn("No books found."); pause(); return
    for b in results:
        print(clr(f"  {b}", GREEN if b.is_available() else RED))
    info(f"{len(results)} result(s) found.")
    pause()

def menu_add_book(lib: Library):
    clear(); header("➕  ADD BOOK")
    title  = prompt("Title")
    author = prompt("Author")
    genre  = prompt("Genre", "General")
    qty    = prompt_int("Quantity", 1)
    if not title or not author:
        err("Title and Author are required."); pause(); return
    book = lib.add_book(title, author, genre, qty)
    ok(f"Book added: {book}")
    pause()

def menu_remove_book(lib: Library):
    clear(); header("🗑️   REMOVE BOOK")
    book_id = prompt("Book ID")
    ok_flag, msg = lib.remove_book(book_id)
    (ok if ok_flag else err)(msg)
    pause()

def menu_update_book(lib: Library):
    clear(); header("✏️   UPDATE BOOK")
    book_id = prompt("Book ID")
    book = lib.books.get(book_id)
    if not book:
        err("Book not found."); pause(); return
    print(clr(f"  Current: {book}", CYAN))
    title  = prompt("New title (Enter to skip)", book.title)
    author = prompt("New author (Enter to skip)", book.author)
    genre  = prompt("New genre (Enter to skip)", book.genre)
    try:
        qty = int(prompt("New quantity (Enter to skip)", str(book.quantity)))
    except ValueError:
        qty = book.quantity
    lib.update_book(book_id, title=title, author=author, genre=genre, quantity=qty,
                    available=book.available + (qty - book.quantity))
    ok("Book updated.")
    pause()


# ─────────────────────────────────────────────────────────────────
#  User menus
# ─────────────────────────────────────────────────────────────────

def menu_view_users(lib: Library):
    clear(); header("👥  ALL USERS")
    users = lib.get_all_users()
    if not users:
        warn("No users registered."); pause(); return
    for u in users:
        print(clr(f"  {u}", CYAN))
    pause()

def menu_register_user(lib: Library, admin_mode: bool = False):
    clear(); header("🆕  REGISTER USER")
    name     = prompt("Full name")
    email    = prompt("Email")
    password = input(clr("  → Password: ", CYAN))
    if not name or not email or not password:
        err("All fields required."); pause(); return
    role = "student"
    if admin_mode:
        role = pick(["student", "admin"], "Role")
    ok_flag, msg, user = lib.register_user(name, email, password, role)
    (ok if ok_flag else err)(msg)
    if user:
        info(f"User ID: {user.id}")
    pause()

def menu_delete_user(lib: Library):
    clear(); header("🗑️   DELETE USER")
    user_id = prompt("User ID")
    ok_flag, msg = lib.delete_user(user_id)
    (ok if ok_flag else err)(msg)
    pause()


# ─────────────────────────────────────────────────────────────────
#  Transaction menus
# ─────────────────────────────────────────────────────────────────

def menu_issue_book(lib: Library, current_user: User):
    clear(); header("📤  ISSUE BOOK")
    book_id = prompt("Book ID")
    user_id = current_user.id if current_user.role == "student" else prompt("User ID")
    ok_flag, msg, txn = lib.issue_book(book_id, user_id)
    (ok if ok_flag else err)(msg)
    if txn:
        info(f"Due date: {txn.due_date} ({txn.days_remaining()} days)")
    pause()

def menu_return_book(lib: Library, current_user: User):
    clear(); header("📥  RETURN BOOK")
    book_id = prompt("Book ID")
    user_id = current_user.id if current_user.role == "student" else prompt("User ID")
    ok_flag, msg, fine = lib.return_book(book_id, user_id)
    (ok if ok_flag else err)(msg)
    if fine:
        warn(f"Fine amount: ৳{fine:.2f} — please pay at the counter.")
    pause()

def menu_view_transactions(lib: Library, current_user: User):
    clear(); header("📋  TRANSACTIONS")
    if current_user.role == "admin":
        choice = pick(["All transactions", "Active only", "Overdue only",
                       "My transactions"], "Filter")
        if choice == "All transactions":
            txns = lib.get_transactions()
        elif choice == "Active only":
            txns = lib.get_transactions(status="active")
        elif choice == "Overdue only":
            txns = lib.get_overdue_transactions()
        else:
            txns = lib.get_transactions(user_id=current_user.id)
    else:
        txns = lib.get_transactions(user_id=current_user.id)

    if not txns:
        warn("No transactions found."); pause(); return
    for t in txns:
        color = RED if (t.status == "active" and t.days_remaining() < 0) else RESET
        print(clr(f"  {t}", color))
    info(f"Total: {len(txns)}")
    pause()


# ─────────────────────────────────────────────────────────────────
#  Dashboard / Report
# ─────────────────────────────────────────────────────────────────

def menu_dashboard(lib: Library):
    clear(); header("📊  LIBRARY DASHBOARD")
    s = lib.summary()
    rows = [
        ("📚 Total titles",       s["total_titles"]),
        ("📦 Total copies",       s["total_copies"]),
        ("✅ Available copies",   s["available_copies"]),
        ("👥 Registered users",  s["total_users"]),
        ("🔄 Active issues",      s["active_issues"]),
        ("⚠️  Overdue issues",    s["overdue_count"]),
        ("💰 Fine collected",     f"৳{s['fine_collected']:.2f}"),
        ("💸 Fine pending",       f"৳{s['fine_pending']:.2f}"),
    ]
    for label, val in rows:
        print(f"  {clr(label, CYAN):<35}  {clr(str(val), YELLOW)}")
    pause()


# ─────────────────────────────────────────────────────────────────
#  Main menus
# ─────────────────────────────────────────────────────────────────

STUDENT_MENU = [
    ("📚 View all books",          menu_view_books),
    ("🔍 Search books",            menu_search_books),
    ("📤 Issue a book",            menu_issue_book),
    ("📥 Return a book",           menu_return_book),
    ("📋 My transactions",         menu_view_transactions),
    ("🚪 Logout",                  None),
]

ADMIN_MENU = [
    ("📚 View all books",          menu_view_books),
    ("🔍 Search books",            menu_search_books),
    ("➕ Add book",                menu_add_book),
    ("✏️  Update book",            menu_update_book),
    ("🗑️  Remove book",            menu_remove_book),
    ("📤 Issue book (for user)",   menu_issue_book),
    ("📥 Return book (for user)",  menu_return_book),
    ("📋 View transactions",       menu_view_transactions),
    ("👥 View all users",          menu_view_users),
    ("🆕 Register user",           menu_register_user),
    ("🗑️  Delete user",            menu_delete_user),
    ("📊 Dashboard / Report",      menu_dashboard),
    ("🚪 Logout",                  None),
]

def run_menu(lib: Library, current_user: User):
    menu = ADMIN_MENU if current_user.role == "admin" else STUDENT_MENU
    while True:
        clear()
        header(f"📖  LIBRARY SYSTEM  |  {current_user.name} ({current_user.role})")
        for i, (label, _) in enumerate(menu, 1):
            print(clr(f"  {i:2}. {label}", CYAN))
        print()
        try:
            choice = int(prompt("Select option")) - 1
            if not (0 <= choice < len(menu)):
                raise ValueError
        except ValueError:
            err("Invalid choice."); pause(); continue

        label, fn = menu[choice]
        if fn is None:                   # Logout
            break
        # functions that need current_user
        if fn in (menu_issue_book, menu_return_book,
                  menu_view_transactions):
            fn(lib, current_user)
        elif fn == menu_register_user and current_user.role == "admin":
            fn(lib, admin_mode=True)
        else:
            fn(lib)


# ─────────────────────────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────────────────────────

def main():
    lib = Library()
    seed_demo_data(lib)

    clear()
    print(clr("""
  ╔══════════════════════════════════════════════════╗
  ║      📚  LIBRARY MANAGEMENT SYSTEM  📚          ║
  ║           Python OOP CLI Edition                 ║
  ║                                                  ║
  ║   Fine rate : ৳5/day after 7-day grace period   ║
  ╚══════════════════════════════════════════════════╝
""", BOLD + BLUE))

    while True:
        user = login_screen(lib)
        run_menu(lib, user)
        clear()
        print(clr(f"\n  👋  Logged out. Goodbye, {user.name}!\n", YELLOW))
        if prompt("Login again? (y/n)", "n").lower() != "y":
            break

    print(clr("\n  📚 Library system closed. All data saved. Bye!\n", GREEN))


if __name__ == "__main__":
    main()
