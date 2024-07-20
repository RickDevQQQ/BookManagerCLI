from enum import Enum
from typing import Type, TypeVar, Generic
import datetime as dt
from dataclasses import dataclass, field

from src.error import TransformError

T = TypeVar('T')


@dataclass(frozen=True)
class Arg(Generic[T]):
    description: str
    type: Type[T]
    required: bool = field(default=False)
    example: str | None = field(default=None)

    def transform(self, value) -> T:
        try:
            return self.type(value)
        except Exception as e:
            raise TransformError(f'Произошла ошибка трансформации, проверьте данные. Ошибка: {e}')


@dataclass(frozen=True)
class StringArg(Arg[str]):
    type: Type[str] = field(default=str)


@dataclass(frozen=True)
class EnumArg(Arg[Enum]):
    type: Type[Enum]


@dataclass(frozen=True)
class DateArg(Arg[dt.date]):
    type: Type[dt.date] = field(default=dt.date)
    example: str = field(default='2024-07-20')

    def transform(self, value) -> dt.date:
        try:
            return dt.date.fromisoformat(value)
        except ValueError as e:
            raise TransformError(f'Произошла ошибка трансформации, проверьте данные. Ошибка: {e}')
