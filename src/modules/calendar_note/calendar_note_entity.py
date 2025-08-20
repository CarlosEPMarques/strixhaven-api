from __future__ import annotations

from datetime import datetime
import uuid

from asyncpg.pgproto import pgproto

from .calendar_note_value_object import (
    CalendarNoteDescription,
    CalendarNoteID,
    CalendarNoteIsExam,
    CalendarNoteTitle,
    CalendarNoteGameDatetime
)


class CalendarNote:
    def __init__(
        self,
        id: CalendarNoteID,
        title: CalendarNoteTitle,
        description: CalendarNoteDescription,
        game_datetime: CalendarNoteGameDatetime,
        is_exam: CalendarNoteIsExam,
    ) -> None:
        self._id = id
        self._title = title
        self._description = description
        self._game_datetime = game_datetime
        self._is_exam = is_exam

    @property
    def id(self) -> str:
        if isinstance(self._id, uuid.UUID):
            return str(self._id)
        if isinstance(self._id, pgproto.UUID):
            return self._id.hex
        return str(self._id)

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def game_datetime(self) -> datetime:
        return self._game_datetime.value

    @property
    def is_exam(self) -> str:
        return self._is_exam.value

    def update_title(self, new_title: CalendarNoteTitle) -> None:
        self._title = new_title

    def update_description(self, new_description: CalendarNoteDescription) -> None:
        self._description = new_description

    def update_game_datetime(self, new_game_datetime: CalendarNoteGameDatetime) -> None:
        self._game_datetime = new_game_datetime

    def update_is_exam(self, new_is_exam: CalendarNoteIsExam) -> None:
        self._is_exam = new_is_exam

    def to_document(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'game_datetime': self.game_datetime,
            'is_exam': self.is_exam,
        }

    @staticmethod
    def from_document(document: dict) -> CalendarNote:
        return CalendarNote(
            id=CalendarNoteID(document['id']),
            title=CalendarNoteTitle(document['title']),
            description=CalendarNoteDescription(document['description']),
            game_datetime=CalendarNoteGameDatetime(document['game_datetime']),
            is_exam=CalendarNoteIsExam(document['is_exam']),
        )

    @staticmethod
    def create(
        title: CalendarNoteTitle,
        description: CalendarNoteDescription,
        game_datetime: CalendarNoteGameDatetime,
        is_exam: CalendarNoteIsExam,
    ) -> CalendarNote:
        return CalendarNote(
            id=CalendarNoteID.generate(),
            title=title,
            description=description,
            game_datetime=game_datetime,
            is_exam=is_exam,
        )
