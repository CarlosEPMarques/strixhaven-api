from datetime import datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.calendar_note.calendar_note_entity import CalendarNote
from src.modules.calendar_note.calendar_note_repository import CalendarNoteRepository
from src.modules.calendar_note.calendar_note_usecase import CalendarNoteUseCase
from src.modules.calendar_note.calendar_note_value_object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)


@pytest.fixture
def calendar_note() -> CalendarNote:
    game_datetime = datetime.fromisoformat('2025-12-01T12:30:00Z')
    calendar_note_title = CalendarNoteTitle('Prismari - Performance Exam')
    calendar_note_description = CalendarNoteDescription('Prismari Building Sector 4 - Class 3')
    calendar_note_game_datetime = CalendarNoteGameDatetime(game_datetime)
    calendar_note_is_exam = CalendarNoteIsExam(value=True)
    return CalendarNote.create(
        title=calendar_note_title,
        description=calendar_note_description,
        game_datetime=calendar_note_game_datetime,
        is_exam=calendar_note_is_exam,
    )


@pytest.fixture
async def calendar_note_2() -> CalendarNote:
    game_datetime = datetime.fromisoformat('2025-12-07T18:30:00Z')
    calendar_note_title = CalendarNoteTitle('Strixhaven Prom Night')
    calendar_note_description = CalendarNoteDescription(
        'Take your best cloths and come to the best night of your life!'
    )
    calendar_note_game_datetime = CalendarNoteGameDatetime(game_datetime)
    calendar_note_is_exam = CalendarNoteIsExam(value=False)
    return CalendarNote.create(
        title=calendar_note_title,
        description=calendar_note_description,
        game_datetime=calendar_note_game_datetime,
        is_exam=calendar_note_is_exam,
    )


@pytest.fixture
def calendar_note_repository(session: AsyncSession) -> CalendarNoteRepository:
    return CalendarNoteRepository(session=session)


@pytest.fixture
def calendar_note_usecase(calendar_note_repository: CalendarNoteRepository) -> CalendarNoteUseCase:
    return CalendarNoteUseCase(calendar_note_repository)
