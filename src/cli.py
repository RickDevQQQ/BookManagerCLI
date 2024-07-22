from typing import Tuple, Mapping, Any, List, Dict

from src.commands.command import TRIGGERS, exit_command
from src.core.command import Command
from src.error import NotFoundCommandError, ApplicationException


def show_start_message() -> None:
    print('CLI BookManager.')
    print('Для получения доп информации можете ввести команду help')
    print('Для выхода можете ввести команду exit')
    print()


class Client:
    def __init__(
        self,
        command_input_text: str = "Введите команду ->",
        command_split: str = ""
    ):
        self.command_input_text = command_input_text
        self.command_split = command_split

    def wait_command(self) -> Tuple[Command, str]:
        """
        Команда ожидает ввод команды и возвращает команду и ввод пользователя.
        Если команда не найдена, то вернет
        """
        client_input = input(self.command_input_text)
        cmd, *client_input = client_input.split(' ')
        client_input = ' '.join(client_input)

        try:
            return TRIGGERS[cmd], client_input
        except KeyError:
            raise NotFoundCommandError(f'Не удалось найти команду - {cmd}')

    def split_command(self):
        print(self.command_split)

    @staticmethod
    def _formatted_args(args: List[str]) -> Mapping[str, Any]:
        """Получить подготовленные и существующие аргументы"""
        result = {}
        for arg in args:
            arg_trigger, *arg_value = arg.split(' ')
            result[arg_trigger] = ' '.join(arg_value)
        return result

    def parse_client_input(self, client_input: str) -> Tuple[str, Mapping[str, Any]]:
        client_input, *args = client_input.split('--')
        args = self._formatted_args(args)
        return client_input, args

    def run(self) -> None:
        show_start_message()
        while True:
            try:
                cmd, client_input = self.wait_command()
                client_input, args = self.parse_client_input(client_input)
                cmd.load_args(args)
                cmd.execute(client_input.strip())
                self.split_command()
            except ApplicationException as e:
                print(e.__doc__, e)
            except KeyboardInterrupt:
                self.split_command()
                exit_command.execute('')
