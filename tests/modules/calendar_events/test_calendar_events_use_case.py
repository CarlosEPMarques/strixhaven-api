from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.exception import (
    CalendarNoteNotFoundException,
    CalendarNotesNotFoundException,
)
from src.modules.calendar_events.repository import CalendarNoteRepository
from src.modules.calendar_events.schema import (
    CalendarNoteCreateInput,
    CalendarNoteOutput,
    CalendarNoteUpdateInput,
)
from src.modules.calendar_events.usecase import CalendarNoteUseCase


async def test_create_calendar_note_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=None)
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.create = AsyncMock()
    input_data = CalendarNoteCreateInput(
        title=calendar_note.title,
        description=calendar_note.description,
        game_datetime=calendar_note.game_datetime,
        is_exam=calendar_note.is_exam,
    )
    created_calendar_note = await calendar_note_usecase.create_calendar_note(input_data)

    assert created_calendar_note.id == calendar_note.id


async def test_update_calendar_note_title_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.update = AsyncMock()
    updated_calendar_note_title = 'Osgir Birthday!'
    updated_calendar_note = await calendar_note_usecase.update_calendar_note(
        calendar_note_id=calendar_note.id,
        input_data=CalendarNoteUpdateInput(title=updated_calendar_note_title),
    )

    assert updated_calendar_note.title == updated_calendar_note_title


async def test_update_calendar_note_description_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.update = AsyncMock()
    updated_calendar_note_description = 'Dont forget about Professor Osgir birthday'
    updated_calendar_note = await calendar_note_usecase.update_calendar_note(
        calendar_note_id=calendar_note.id,
        input_data=CalendarNoteUpdateInput(description=updated_calendar_note_description),
    )

    assert updated_calendar_note.description == updated_calendar_note_description


async def test_update_calendar_note_game_datetime_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.update = AsyncMock()
    updated_game_datetime = datetime.fromisoformat('2020-05-14T18:00:00Z')
    updated_calendar_note = await calendar_note_usecase.update_calendar_note(
        calendar_note_id=calendar_note.id,
        input_data=CalendarNoteUpdateInput(game_datetime=updated_game_datetime),
    )

    assert updated_calendar_note.game_datetime == updated_game_datetime


async def test_update_calendar_note_is_exam_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.update = AsyncMock()
    updated_calendar_note_is_exam = False
    updated_calendar_note = await calendar_note_usecase.update_calendar_note(
        calendar_note_id=calendar_note.id,
        input_data=CalendarNoteUpdateInput(is_exam=updated_calendar_note_is_exam),
    )

    assert updated_calendar_note.is_exam == updated_calendar_note_is_exam


async def test_update_calendar_note_not_found_usecase(
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=None)

    with pytest.raises(CalendarNoteNotFoundException) as error:
        await calendar_note_usecase.update_calendar_note(
            calendar_note_id='random-id', input_data=CalendarNoteUpdateInput()
        )

    assert str(error.value) == CalendarNoteNotFoundException.detail


async def test_delete_calendar_note_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    calendar_note_repository.delete = AsyncMock()
    await calendar_note_usecase.delete_calendar_note(calendar_note.id)

    calendar_note_repository.delete.assert_awaited_once_with(calendar_note)


async def test_delete_calendar_note_usecase_not_found(
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=None)

    with pytest.raises(CalendarNoteNotFoundException) as error:
        await calendar_note_usecase.delete_calendar_note('random-id')

    assert str(error.value) == CalendarNoteNotFoundException.detail


async def test_find_calendar_note_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=calendar_note)
    result = await calendar_note_usecase.find_calendar_note_by_id(calendar_note.id)

    assert result == CalendarNoteOutput.from_entity(calendar_note)


async def test_find_calendar_note_usecase_not_found(
    calendar_note_usecase: CalendarNoteUseCase, calendar_note_repository: CalendarNoteRepository
) -> None:
    calendar_note_repository.find = AsyncMock(return_value=None)

    with pytest.raises(CalendarNoteNotFoundException) as error:
        await calendar_note_usecase.find_calendar_note_by_id('non-existent-id')

    assert str(error.value) == CalendarNoteNotFoundException.detail


async def test_find_calendar_notes_usecase(
    calendar_note: CalendarNote,
    calendar_note_usecase: CalendarNoteUseCase,
    calendar_note_repository: CalendarNoteRepository,
) -> None:
    calendar_note_repository.find_all = AsyncMock(return_value=[calendar_note])
    result = await calendar_note_usecase.find_calendar_notes()

    assert len(result) == 1


async def test_find_calendar_notes_usecase_not_found(
    calendar_note_usecase: CalendarNoteUseCase, calendar_note_repository: CalendarNoteRepository
) -> None:
    calendar_note_repository.find_all = AsyncMock(return_value=None)

    with pytest.raises(CalendarNotesNotFoundException) as error:
        await calendar_note_usecase.find_calendar_notes()

    assert str(error.value) == CalendarNotesNotFoundException.detail
