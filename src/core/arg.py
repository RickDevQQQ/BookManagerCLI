from abc import ABC
from enum import Enum
from typing import Type, TypeVar, Generic, Optional, Any
import datetime as dt
from src.error import TransformError

T = TypeVar('T')


class Arg(Generic[T], ABC):

    def __init__(
        self,
        default: Any = None,
        arg_type: Type[T] = str,
        required: bool = False,
        description: Optional[str] = None,
        example: Optional[str] = None
    ):
        self._value = default
        self._arg_type = arg_type
        self._required = required
        self._description = description
        self._example = example

    @property
    def value(self) -> Optional[T]:
        if self._value is None:
            return None
        try:
            return self._arg_type(self._value)
        except Exception as e:
            raise TransformError(f'Произошла ошибка трансформации, проверьте данные. Ошибка: {e}')

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    @property
    def required(self) -> bool:
        return self._required

    @property
    def description(self) -> Optional[str]:
        return self._description

    @property
    def example(self) -> Optional[str]:
        return self._example

    @property
    def arg_type(self):
        return self._arg_type


class EnumArg(Arg[Enum]):

    def __init__(
        self,
        default: Any = None,
        arg_type: Type[Enum] = str,
        required: bool = False,
        description: Optional[str] = None,
        example: Optional[str] = None
    ):
        super().__init__(
            default=default,
            arg_type=arg_type,
            required=required,
            description=description,
            example=example
        )

    def get_values(self):
        """Получить возможные аргументы ENUM"""
        pass


class DateArg(Arg[dt.date]):

    def __init__(
        self,
        default: Any = None,
        required: bool = False,
        description: Optional[str] = None,
        example: Optional[str] = None
    ):
        super().__init__(
            default=default,
            arg_type=dt.date,
            required=required,
            description=description,
            example=example
        )

    @property
    def value(self) -> Optional[T]:
        if self._value is None:
            return None
        try:
            return self._arg_type.fromisoformat(self._value)
        except Exception as e:
            raise TransformError(f'Произошла ошибка трансформации, проверьте данные. Ошибка: {e}')

