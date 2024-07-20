from abc import ABC, abstractmethod
from typing import Mapping, Tuple, List, Dict, Any

from src.core.arg import Arg
from src.error import MissingRequiredArgsError


class Command(ABC):

    def __init__(
        self,
        full_name: str,
        description: str | None = None,
        args: Mapping[str, Arg] | None = None,
        other_trigger_name: Tuple | None = None
    ):
        self.full_name = full_name
        self.description = description
        self.args = args if args else {}
        self.other_trigger_name = other_trigger_name if other_trigger_name else tuple()

    def get_required_args(self) -> List[Arg]:
        """Получить список обязательных аргументов"""
        return list(filter(lambda arg: arg.required, self.args))

    def _validate_args(self, args: Dict[Arg, Any]):
        """Валидация аргументов"""
        required_args = self.get_required_args()
        missing_args = []

        for arg in required_args:
            if arg not in args:
                missing_args.append(arg)

        if missing_args:
            text = ' '.join([k.description for k in args.keys()])
            raise MissingRequiredArgsError(f'Были пропущены следующие аргументы: {text}')

    def _formatted_args(self, args: List[str]) -> Dict[Arg, Any]:
        """Получить подготовленные и существующие аргументы"""
        result = {}
        for arg in args:
            arg_trigger, *arg_value = arg.split(' ')

            try:
                arg_object = self.args[arg_trigger]
            except KeyError:
                continue

            result[arg_object] = arg_object.transform(' '.join(arg_value))
        self._validate_args(result)
        return result

    def parse_client_input(self, client_input: str) -> Tuple[str, Dict[Arg, Any]]:
        client_input, *args = client_input.split('--')
        args = self._formatted_args(args)
        return client_input, args

    @abstractmethod
    def execute(self, client_input: str, **kwargs: Dict[Arg, Any]) -> None:
        ...
