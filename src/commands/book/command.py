from src.commands.book.dto import CreateBookDTO, UpdateBookDTO
from src.commands.book.enum import BookStatus
from src.commands.book.service import BookService
from src.core.arg import Arg, EnumArg, DateArg
from src.core.command import Command

book_service = BookService()


class AddBookCommand(Command):
    full_name = 'add-book'
    description = 'Добавить книгу'
    other_trigger_name = ('ab', 'abook')

    title = Arg(required=True, description="Заголовок книги", example="Лучшая книга в мире")
    year = DateArg(required=True, description="Год выпуска")
    author = Arg(required=True, description="Автор")
    status = EnumArg(required=True, arg_type=BookStatus, description="Статус книги")

    def execute(self, client_input: str) -> None:
        book = book_service.save(
            dto=CreateBookDTO(
                title=self.title.value,
                year=self.year.value,
                author=self.author.value,
                status=self.status.value
            )
        )
        print(f"Успешно создалась книга. UUID - {book.uuid}")


class RemoveBookCommand(Command):
    full_name = 'remove-book'
    description = 'Удалить книгу. Укажи сразу после команды UUID книги'
    other_trigger_name = ('rb', 'rbook')

    def execute(self, value: str) -> None:
        book_service.delete(value)
        print(f'Успешно удалена книга. UUID - {value}')


class GetAllBookCommand(Command):
    full_name = 'all-book'
    description = "Получить список всех книг"

    def execute(self, value: str) -> None:
        books = book_service.get_all()
        print("Список всех книг:")
        for book in books:
            print(book)


class ChangeStatusBookCommand(Command):
    full_name = 'change-status-book'
    description = "Сменить статус книги. Укажи сразу после команды UUID книги"

    status = EnumArg(required=True, arg_type=BookStatus, description="Статус книги")

    def execute(self, value: str) -> None:
        book_service.update(uuid=value, dto=UpdateBookDTO(status=self.status.value))
        print(f'Успешно изменен статус книги. UUID - {value}')


class SearchBookCommand(Command):
    full_name = 'search-book'
    description = "Поиск книг"

    title = Arg(description="Поиск по заголовку книги")
    author = Arg(description="Поиск по автору")
    year = Arg(description="Поиск по году выпуска")

    def execute(self, value: str) -> None:
        books = book_service.get_all(author=self.author.value, title=self.title.value, year=self.year.value)
        print("Список найденных книг:")
        for book in books:
            print(book)
