from typing import Any, Dict

from src.commands.book.command import add_book_command
from src.core.arg import Arg, EnumArg
from src.core.command import Command
from src.commands.system.command import exit_command


class HelpCommand(Command):

    @staticmethod
    def args_info(cmd: Command) -> None:
        print(f'Поддерживает следующие аргументы:')
        for key, arg in cmd.args.items():
            text = f'{'[*]' if arg.required else '[ ]'} {key}. {arg.description} '
            if arg.example:
                text += f'[Пример: {arg.example}] '
            if isinstance(arg, EnumArg):
                values = ', '.join([member.value for member in arg.type.__members__.values()])
                text += f"\n\t ~ Поддерживает следующие значения: [{values}]"
            print(text)

    def all_command(self):
        print('Список всех команд')
        for index, cmd in enumerate(COMMANDS, start=1):
            text = f'{cmd.full_name} {cmd.description} '

            if cmd.other_trigger_name:
                text += f'[Сокращения: {', '.join(cmd.other_trigger_name)}]'

            print(text)

            if cmd.args:
                self.args_info(cmd)

    def execute(self, client_input: str, **kwargs: Dict[Arg, Any]) -> None:
        self.all_command()


help_command = HelpCommand(
    full_name='help',
    description='Получить подробную информацию',
    other_trigger_name=('h',)
)
COMMANDS = (
    help_command,
    exit_command,
    add_book_command
)
TRIGGERS = {}
for command in COMMANDS:
    TRIGGERS[command.full_name] = command

    if command.other_trigger_name is None:
        continue

    for other_trigger in command.other_trigger_name:
        TRIGGERS[other_trigger] = command
