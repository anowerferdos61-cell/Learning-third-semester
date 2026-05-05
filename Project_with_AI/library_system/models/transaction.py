from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

FINE_RATE_PER_DAY = 5.00   # BDT per day after grace period
GRACE_DAYS = 7


@dataclass
class Transaction:
    id: str
    book_id: str
    user_id: str
    issue_date: str          # ISO format "YYYY-MM-DD"
    due_date: str
    return_date: Optional[str] = None
    fine: float = 0.0
    status: str = "active"   # "active" | "returned"

    # ── fine calculation ──────────────────────────────────────────
    def calculate_fine(self, return_on: Optional[date] = None) -> float:
        ret = return_on or date.today()
        due = date.fromisoformat(self.due_date)
        if ret > due:
            days_late = (ret - due).days
            return round(days_late * FINE_RATE_PER_DAY, 2)
        return 0.0

    def close(self, return_on: Optional[date] = None) -> float:
        ret = return_on or date.today()
        self.return_date = ret.isoformat()
        self.fine = self.calculate_fine(ret)
        self.status = "returned"
        return self.fine

    def days_remaining(self) -> int:
        """Positive = days left, negative = overdue days"""
        due = date.fromisoformat(self.due_date)
        return (due - date.today()).days

    # ── serialisation ─────────────────────────────────────────────
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "issue_date": self.issue_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "fine": self.fine,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(
            id=data["id"],
            book_id=data["book_id"],
            user_id=data["user_id"],
            issue_date=data["issue_date"],
            due_date=data["due_date"],
            return_date=data.get("return_date"),
            fine=data.get("fine", 0.0),
            status=data.get("status", "active"),
        )

    def __str__(self) -> str:
        days = self.days_remaining()
        if self.status == "returned":
            fine_str = f"Fine: ৳{self.fine:.2f}" if self.fine else "No fine"
            return (
                f"[{self.id}] Book:{self.book_id} | User:{self.user_id} | "
                f"Issued:{self.issue_date} → Returned:{self.return_date} | {fine_str}"
            )
        overdue = f"⚠️  {-days}d overdue" if days < 0 else f"⏳ {days}d left"
        pending_fine = self.calculate_fine()
        fine_note = f" | Pending fine: ৳{pending_fine:.2f}" if pending_fine else ""
        return (
            f"[{self.id}] Book:{self.book_id} | User:{self.user_id} | "
            f"Issued:{self.issue_date} | Due:{self.due_date} | {overdue}{fine_note}"
        )
