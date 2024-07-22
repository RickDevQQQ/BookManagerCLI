from src.commands.book.enum import BookStatus
from dataclasses import dataclass, field
import datetime as dt


@dataclass(frozen=True)
class CreateBookDTO:
    title: str
    status: BookStatus
    author: str
    year: dt.date


@dataclass(frozen=True)
class UpdateBookDTO(CreateBookDTO):
    title: str | None = field(default=None)
    status: BookStatus | None = field(default=None)
    author: str | None = field(default=None)
    year: dt.date | None = field(default=None)


@dataclass()
class BookDTO:
    uuid: str
    title: str
    status: BookStatus
    author: str
    year: dt.date
