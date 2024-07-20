from src.commands.book.enum import BookStatus
from dataclasses import dataclass
import datetime as dt


@dataclass(frozen=True)
class CreateBookDTO:
    title: str
    status: BookStatus
    author: str
    year: dt.date


@dataclass(frozen=True)
class UpdateBookDTO(CreateBookDTO):
    title: str | None
    status: BookStatus | None
    author: str | None
    year: dt.date | None


@dataclass(frozen=True)
class BookDTO:
    uuid: str
    title: str
    status: BookStatus
    author: str
    year: dt.date
