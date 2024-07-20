import json
from abc import ABC, abstractmethod
from typing import Any, Dict
import os


class AbstractStorage(ABC):

    @abstractmethod
    def insert(self, key: str, value: Any) -> None:
        ...

    @abstractmethod
    def get(self, key: str) -> Any:
        ...

    @abstractmethod
    def delete(self, key: str) -> None:
        ...


class JsonStorage:
    def __init__(self, filename: str):
        self.filename = filename
        self._check_file_exists()

    def _check_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({}, file)

    def _load_data(self) -> Dict[str, Any]:
        with open(self.filename, 'r') as file:
            return json.load(file)

    def _write_data(self, data: Dict[str, Any]):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def insert(self, key: str, value: Any) -> None:
        data = self._load_data()
        data[key] = value
        self._write_data(data)

    def get(self, key: str) -> Any:
        data = self._load_data()
        return data.get(key)

    def get_all(self):
        return self._load_data()

    def delete(self, key: str) -> None:
        data = self._load_data()
        del data[key]
        self._write_data(data)
