from typing import List, Dict
from uuid import uuid4

from src.commands.book.dto import CreateBookDTO, BookDTO, UpdateBookDTO
from src.commands.book.mapper import BookMapper
from src.core.storage import JsonStorage
from src.error import NotFoundEntityError


class BookService:
    def __init__(self):
        self.book_storage = JsonStorage('books.json')

    def _get_by_uuid(self, uuid) -> Dict:
        book = self.book_storage.get(key=uuid)
        if not book:
            raise NotFoundEntityError(f'Ну удалось найти сущность по uuid - {uuid}')
        return book

    def generate_unique_uuid(self):
        uuid = str(uuid4())
        if self.book_storage.get(uuid):
            uuid = self.generate_unique_uuid()
        return uuid

    def save(self, dto: CreateBookDTO) -> BookDTO:
        uuid = self.generate_unique_uuid()
        value = BookMapper.from_create_dto_to_storage_dict(uuid, dto)
        self.book_storage.insert(key=uuid, value=value)
        return BookMapper.from_dict_to_dto(value)

    def get_by_uuid(self, uuid: str) -> BookDTO:
        return BookMapper.from_dict_to_dto(self._get_by_uuid(uuid))

    def get_all(
        self,
        title: str = '',
        author: str = '',
        year: str = '',
    ) -> List[BookDTO]:
        return [
            BookMapper.from_dict_to_dto(item)
            for item in filter(
                lambda item:
                title in item['title'] and
                author in item['author'] and
                year in item['year'],
                self.book_storage.get_all().values()
            )
        ]

    def update(self, uuid: str, dto: UpdateBookDTO) -> BookDTO:
        book = BookMapper.from_dict_to_dto(self._get_by_uuid(uuid))

        value = {
            'uuid': uuid,
            'title': book.title if dto.title is None else dto.title,
            'status': book.status if dto.status is None else dto.status,
            'year': book.year if dto.year is None else dto.year,
            'author': book.author if dto.author is None else dto.author
        }
        self.book_storage.insert(key=uuid, value=value)
        return BookMapper.from_dict_to_dto(value)

    def delete(self, uuid: str) -> None:
        _ = BookMapper.from_dict_to_dto(self._get_by_uuid(uuid))
        self.book_storage.delete(uuid)
