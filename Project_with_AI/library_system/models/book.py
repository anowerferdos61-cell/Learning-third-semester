from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Book:
    id: str
    title: str
    author: str
    genre: str
    quantity: int
    available: int

    def is_available(self) -> bool:
        return self.available > 0

    def update_stock(self, delta: int) -> bool:
        """delta = +1 for return, -1 for issue"""
        new_val = self.available + delta
        if new_val < 0 or new_val > self.quantity:
            return False
        self.available = new_val
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "quantity": self.quantity,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            genre=data.get("genre", "General"),
            quantity=data["quantity"],
            available=data["available"],
        )

    def __str__(self) -> str:
        status = f"✅ {self.available}/{self.quantity}" if self.is_available() else "❌ Out of Stock"
        return (
            f"[{self.id}] '{self.title}' by {self.author} "
            f"| Genre: {self.genre} | Stock: {status}"
        )
