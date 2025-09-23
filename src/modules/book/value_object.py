from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

import regex as re

from src.modules.book.exception import (
    BookInvalidImageUrlException,
    BookInvalidIsHiddenException,
    BookInvalidSectionException,
    BookInvalidSummaryException,
    BookInvalidTitleException,
)


@dataclass(frozen=True)
class BookID:
    value: str

    @staticmethod
    def generate() -> BookID:
        return BookID(str(uuid4()))

    @staticmethod
    def from_uuid(id: UUID) -> BookID:
        return BookID(str(id))

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class BookTitle:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(
            r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value
        ):
            raise BookInvalidTitleException(title=self.value)


@dataclass(frozen=True)
class BookSummary:
    value: str
    _MIN_CHARACTERS: int = 10
    _MAX_CHARACTERS: int = 5000

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not (
            self._MIN_CHARACTERS <= len(self.value) <= self._MAX_CHARACTERS
        ):
            raise BookInvalidSummaryException(summary=self.value)


@dataclass(frozen=True)
class BookSection:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(
            r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value
        ):
            raise BookInvalidSectionException(section=self.value)


@dataclass(frozen=True)
class BookIsHidden:
    value: bool

    def __post_init__(self) -> None:
        if not isinstance(self.value, bool):
            raise BookInvalidIsHiddenException(is_hidden=self.value)


@dataclass(frozen=True)
class BookImageUrl:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise BookInvalidImageUrlException(image_url=self.value)

        if not re.match(r'^https?://[^\s/$.?#].[^\s]*$', self.value):
            raise BookInvalidImageUrlException(image_url=self.value)
