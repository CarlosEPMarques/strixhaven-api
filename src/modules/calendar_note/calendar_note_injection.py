from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.calendar_note.calendar_note_repository import CalendarNoteRepository
from src.modules.calendar_note.calendar_note_usecase import CalendarNoteUseCase
from src.settings.database.sqlalchemy.database import get_session


def calendar_note_usecase_factory(
    database: AsyncSession = Depends(get_session),
) -> CalendarNoteUseCase:
    calendar_note_repository = CalendarNoteRepository(database)
    return CalendarNoteUseCase(calendar_note_repository)
