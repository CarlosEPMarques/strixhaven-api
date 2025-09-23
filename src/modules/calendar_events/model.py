from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, String, Text
from sqlalchemy.types import DateTime as DateTimeType

from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.value_object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteID,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)
from src.settings.database.sqlalchemy import Base


class CalendarNoteModel(Base):
    __tablename__ = 'calendar_events'

    external_id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    game_datetime: Mapped[datetime] = mapped_column(DateTimeType(timezone=True), nullable=True)
    is_exam: Mapped[bool] = mapped_column(Boolean, server_default=text('FALSE'), nullable=False)

    def to_entity(self) -> CalendarNote:
        return CalendarNote(
            id=CalendarNoteID(str(self.external_id)),
            title=CalendarNoteTitle(self.title),
            description=CalendarNoteDescription(self.description),
            game_datetime=CalendarNoteGameDatetime(self.game_datetime),
            is_exam=CalendarNoteIsExam(self.is_exam),
        )

    @staticmethod
    def from_entity(calendar_note: CalendarNote) -> CalendarNoteModel:
        return CalendarNoteModel(
            external_id=calendar_note.id,
            title=calendar_note.title,
            description=calendar_note.description,
            game_datetime=calendar_note.game_datetime,
            is_exam=calendar_note.is_exam,
        )
