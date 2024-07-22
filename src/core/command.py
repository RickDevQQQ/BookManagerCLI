from abc import ABC, abstractmethod
from typing import Mapping, Tuple, List, Dict, Any, TYPE_CHECKING

from src.core.arg import Arg
from src.error import MissingRequiredArgsError


class Command(ABC):
    full_name: str
    description: str | None = None
    other_trigger_name = tuple()

    __command_args__: Mapping[str, Arg] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        children = {}
        for base in reversed(cls.__mro__):
            for name, member in base.__dict__.items():
                if isinstance(member, Arg):
                    children[name] = member

        cls.__command_args__ = children

    def validate_args(self):
        """Валидация аргументов"""
        missing_required_args = list(
            filter(lambda item: item[1].required and item[1].value is None, self.__command_args__.items())
        )
        if missing_required_args:
            text = ', '.join([f'{name} [{arg.description}]' for name, arg in missing_required_args])
            raise MissingRequiredArgsError(
                f'Были пропущены следующие аргументы: {text}'
            )

    def load_args(self, kwargs: Mapping[str, Any]) -> None:
        """Загрузить значения в Args"""
        for key, value in kwargs.items():
            arg = self.__command_args__.get(key)
            if not arg:
                continue
            arg.value = value
        self.validate_args()

    @abstractmethod
    def execute(self, value: str) -> None:
        ...

#
# class DefaultCommand(Command):
#     a = Arg(required=True, description="asddas", example="Asdasd")
#
# class MyCommand(DefaultCommand):
#     full_name = 'my-command'
#     description = 'asdasd'
#     other_trigger_name = ('asd',)
#     title = Arg(required=True, description="Заголовок книги", example="Супер пупер книга")
#
#     def execute(self, value: str) -> None:
#         print(self.title.value)
#
# a = MyCommand()
# a.load_args({'titlea': 'asdas'})
# a.execute('asdasd')
