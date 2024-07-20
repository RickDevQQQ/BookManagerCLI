from typing import Dict

from src.commands.book.dto import BookDTO, CreateBookDTO
import datetime as dt


class BookMapper:

    @staticmethod
    def from_dict_to_dto(data: Dict) -> BookDTO:
        return BookDTO(
            uuid=data['uuid'],
            title=data['title'],
            status=data['status'],
            year=dt.date.fromisoformat(data['year']),
            author=data['author']
        )

    @staticmethod
    def from_create_dto_to_storage_dict(uuid: str, dto: CreateBookDTO) -> Dict:
        return {
            'uuid': uuid,
            'title': dto.title,
            'status': dto.status,
            'year': dto.year,
            'author': dto.author,
        }
