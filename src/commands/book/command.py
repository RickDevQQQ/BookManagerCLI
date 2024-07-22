from src.commands.book.enum import BookStatus
from src.commands.book.service import BookService
from src.core.arg import Arg, EnumArg, DateArg
from src.core.command import Command


book_service = BookService()


class AddBookCommand(Command):
    full_name = 'add-book'
    description = 'Добавить книгу'
    other_trigger_name = ('ad', 'abook')

    title = Arg(required=True, description="Заголовок книги", example="Лучшая книга в мире")
    year = DateArg(required=True, description="Год выпуска")
    author = Arg(required=True, description="Автор")
    status = EnumArg(required=True, arg_type=BookStatus, description="Статус книги")

    def execute(self, client_input: str) -> None:
        book_service.save()
