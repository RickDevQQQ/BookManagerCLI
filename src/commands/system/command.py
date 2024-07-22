from typing import Any

from typing_extensions import Dict

from src.core.arg import Arg
from src.core.command import Command


class ExitCommand(Command):
    full_name = 'exit'
    description = "Покинуть приложение"
    other_trigger_name = ('e',)

    def execute(self, client_input: str, **kwargs: Dict[Arg, Any]) -> None:
        print("Благодарю за использование CLI Book Manager!")
        print("До скорой встречи!:)")
        print('<3')
        exit()
