import json
import os
from typing import Any

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def _path(filename: str) -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, filename)


def load_json(filename: str) -> Any:
    path = _path(filename)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_json(filename: str, data: Any) -> None:
    with open(_path(filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
