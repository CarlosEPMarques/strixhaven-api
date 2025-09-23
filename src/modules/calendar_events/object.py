from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

import regex as re

from src.modules.calendar_events.exception import (
    CalendarNoteInvalidDatetimeException,
    CalendarNoteInvalidDescriptionException,
    CalendarNoteInvalidIsExamException,
    CalendarNoteInvalidTitleException,
)


@dataclass(frozen=True)
class CalendarNoteID:
    value: str

    @staticmethod
    def generate() -> CalendarNoteID:
        return CalendarNoteID(str(uuid4()))

    @staticmethod
    def from_uuid(id: UUID) -> CalendarNoteID:
        return CalendarNoteID(str(id))

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class CalendarNoteTitle:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.match(
            r'^[\p{L}\p{N}\s.,!?\'"-]{2,100}$', self.value
        ):
            raise CalendarNoteInvalidTitleException(title=self.value)


@dataclass(frozen=True)
class CalendarNoteDescription:
    value: str
    _MIN_CHARACTERS: int = 10
    _MAX_CHARACTERS: int = 5000

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not (
            self._MIN_CHARACTERS <= len(self.value) <= self._MAX_CHARACTERS
        ):
            raise CalendarNoteInvalidDescriptionException(description=self.value)


@dataclass(frozen=True)
class CalendarNoteGameDatetime:
    value: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise CalendarNoteInvalidDatetimeException(datetime=str(self.value))

    def __str__(self) -> str:
        return self.value.strftime('%Y-%m-%dT%H:%M:%S+00:00')


@dataclass(frozen=True)
class CalendarNoteIsExam:
    value: bool

    def __post_init__(self) -> None:
        if not isinstance(self.value, bool):
            raise CalendarNoteInvalidIsExamException(is_exam=self.value)
