from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

import regex as re

from src.modules.classes.exception import (
    ClassInvalidNameException,
    ClassInvalidDescriptionException,
    ClassInvalidCollegeIdException,
    ClassInvalidImageUrlException,
)

@dataclass(frozen=True)
class ClassID:
    value: str

    @staticmethod
    def generate() -> ClassID:
        return ClassID(str(uuid4()))

    @staticmethod
    def from_uuid(id: UUID) -> ClassID:
        return ClassID(str(id))

    def __str__(self) -> str:
        return self.value
    
@dataclass(frozen=True)
class ClassName:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(
            r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value
        ):
            raise ClassInvalidNameException(name=self.value)


@dataclass(frozen=True)
class ClassDescription:
    value: str
    _MIN_CHARACTERS: int = 10
    _MAX_CHARACTERS: int = 5000

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not (
            self._MIN_CHARACTERS <= len(self.value) <= self._MAX_CHARACTERS
        ):
            raise ClassInvalidDescriptionException(description=self.value)

@dataclass(frozen=True)
class ClassCollegeID:
    value: int

    def __post_init__(self) -> None:
        if not isinstance(self.value, int):
            raise ClassInvalidCollegeIdException
        
@dataclass(frozen=True)
class ClassImageUrl:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise ClassInvalidImageUrlException(image_url=self.value)

        if not re.match(r'^https?://[^\s/$.?#].[^\s]*$', self.value):
            raise ClassInvalidImageUrlException(image_url=self.value)
