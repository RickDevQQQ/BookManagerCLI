from typing import Tuple, Any, Dict
from uuid import uuid4
from src.commands.book.enum import BookStatus
from src.commands.book.service import BookService
from src.core.arg import Arg, StringArg, EnumArg, DateArg
from src.core.command import Command


book_service = BookService()


class AddBookCommand(Command):

    def execute(self, client_input: str, **kwargs: Dict[Arg, Any]) -> None:

        title_arg = self.args['title']
        title_value = kwargs.get(title_arg, None)
        if title_value is None:
            pass
        book_service.save(

        )


add_book_command = AddBookCommand(
    full_name='add-book',
    description="Добавить книгу",
    other_trigger_name=('ad', 'abook'),
    args={
        'title': StringArg(
            description='Заголовок Книги',
            required=True
        ),
        'status': EnumArg(
            type=BookStatus,
            description='Статус книги',
            required=True
        ),
        'author': StringArg(
            description="Автор",
            required=True
        ),
        'year': DateArg(
            description="Год выпуска",
            required=True
        )
    }
)
