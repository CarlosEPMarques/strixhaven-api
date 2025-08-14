from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4
import regex as re

from src.modules.book.book_exception import (
    BookInvalidIsHiddenException,
    BookInvalidImageUrlException,
    BookInvalidSectionException,
    BookInvalidSummaryException,
    BookInvalidTitleException
)

@dataclass(frozen=True)
class BookID:
    value: str

    @staticmethod
    def generate() -> BookID:
        return BookID(str(uuid4()))
    
    @staticmethod
    def from_uuid(id) -> BookID:
        return BookID(str(id))

    def __str__(self) -> str:
        return self.value

@dataclass(frozen=True)
class BookTitle:
    value: str
    
    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value):
            raise BookInvalidTitleException

@dataclass(frozen=True)
class BookSummary:
    value: str
    
    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not (10 <= len(self.value) <= 5000):
            raise BookInvalidSummaryException

@dataclass(frozen=True)
class BookSection:
    value: str
    
    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value):
            raise BookInvalidSectionException

@dataclass(frozen=True)
class BookIsHidden:
    value: bool    

    def __post_init__(self) -> None:
        if not isinstance(self.value, bool):
            raise BookInvalidIsHiddenException
    
@dataclass(frozen=True)
class BookImageUrl:
    value: str
    
    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise BookInvalidImageUrlException

        if not re.match(r'^https?://[^\s/$.?#].[^\s]*$', self.value):
            raise BookInvalidImageUrlException