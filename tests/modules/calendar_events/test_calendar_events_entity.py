from datetime import datetime

from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)


def test_constructor_should_create_instance(calendar_note: CalendarNote) -> None:
    game_datetime = calendar_note.game_datetime.strftime('%Y-%m-%dT%H:%M:%S')
    assert calendar_note.id is not None
    assert calendar_note.title == 'Prismari - Performance Exam'
    assert calendar_note.description == 'Prismari Building Sector 4 - Class 3'
    assert game_datetime == '2025-12-01T12:30:00'
    assert calendar_note.is_exam is True


def test_update_calendar_note_title(calendar_note: CalendarNote) -> None:
    calendar_note.update_title(CalendarNoteTitle('Strixhaven Interclass - Acting'))
    assert calendar_note.title == 'Strixhaven Interclass - Acting'


def test_update_calendar_note_description(calendar_note: CalendarNote) -> None:
    calendar_note.update_description(
        CalendarNoteDescription('The presentation will occur in the Stadium!')
    )
    assert calendar_note.description == 'The presentation will occur in the Stadium!'


def test_update_calendar_note_game_datetime(calendar_note: CalendarNote) -> None:
    updated_game_datetime = datetime.fromisoformat('2020-05-14T18:00:00Z')
    calendar_note.update_game_datetime(CalendarNoteGameDatetime(updated_game_datetime))
    game_datetime = calendar_note.game_datetime.strftime('%Y-%m-%dT%H:%M:%S')
    assert game_datetime == '2020-05-14T18:00:00'


def test_update_calendar_note_is_exam(calendar_note: CalendarNote) -> None:
    calendar_note.update_is_exam(CalendarNoteIsExam(value=True))
    assert calendar_note.is_exam is True
