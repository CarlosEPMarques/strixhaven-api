from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.repository import CalendarNoteRepository
from src.modules.calendar_events.object import CalendarNoteTitle


async def test_crud_calendar_note(
    calendar_note_repository: CalendarNoteRepository, calendar_note: CalendarNote
) -> None:
    # Create
    await calendar_note_repository.find(calendar_note.id)
    await calendar_note_repository.create(calendar_note)
    created_calendar_note = await calendar_note_repository.find(calendar_note.id)
    assert created_calendar_note is not None

    # Read
    found_calendar_note = await calendar_note_repository.find(calendar_note.id)
    assert found_calendar_note is not None
    assert found_calendar_note.title == calendar_note.title

    # Update
    new_title = 'Strixhaven Interclass - Acting Conquest!'
    found_calendar_note.update_title(CalendarNoteTitle(new_title))
    await calendar_note_repository.update(found_calendar_note)
    updated_calendar_note = await calendar_note_repository.find(found_calendar_note.id)
    assert updated_calendar_note is not None
    assert updated_calendar_note.title == found_calendar_note.title

    # Delete
    await calendar_note_repository.delete(updated_calendar_note)
    deleted_calendar_note = await calendar_note_repository.find(updated_calendar_note.id)
    assert deleted_calendar_note is None
