from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.value_object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)


class CalendarNoteCreateInput(BaseModel):
    title: str = Field(examples=['Lorehold - Museology Exam'])
    description: str = Field(examples=['Final Exams'])
    game_datetime: datetime = Field(examples=['2025-12-01T12:00:00Z'])
    is_exam: bool = Field(examples=[True])

    def to_entity(self) -> CalendarNote:
        return CalendarNote.create(
            title=CalendarNoteTitle(self.title),
            description=CalendarNoteDescription(self.description),
            game_datetime=CalendarNoteGameDatetime(self.game_datetime),
            is_exam=CalendarNoteIsExam(self.is_exam),
        )


class CalendarNoteUpdateInput(BaseModel):
    title: str | None = Field(default=None, examples=['Lorehold - Museology Exam'])
    description: str | None = Field(default=None, examples=['Final Exams'])
    game_datetime: datetime | None = Field(default=None, examples=['2025-12-01T12:00:00Z'])
    is_exam: bool | None = Field(default=None, examples=[True])


class CalendarNoteOutput(BaseModel):
    id: str = Field(examples=['casQJWEqkohQE5643HRcmxnRT'])
    title: str = Field(examples=['Lorehold - Museology Exam'])
    description: str = Field(examples=['Final Exams'])
    game_datetime: datetime = Field(examples=['2025-12-01T12:00:00Z'])
    is_exam: bool = Field(examples=[True])

    @staticmethod
    def from_entity(calendar_note: CalendarNote) -> CalendarNoteOutput:
        return CalendarNoteOutput(
            id=calendar_note.id,
            title=calendar_note.title,
            description=calendar_note.description,
            game_datetime=calendar_note.game_datetime,
            is_exam=calendar_note.is_exam,
        )
