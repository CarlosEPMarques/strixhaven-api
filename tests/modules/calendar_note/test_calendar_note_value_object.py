from datetime import datetime
import pytest

from src.modules.calendar_note.calendar_note_exception import (
    CalendarNoteInvalidDatetimeException,
    CalendarNoteInvalidDescriptionException,
    CalendarNoteInvalidIsExamException,
    CalendarNoteInvalidTitleException,
)
from src.modules.calendar_note.calendar_note_value_object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteID,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)


# ID
def test_calendar_note_id_constructor_should_create_instance() -> None:
    value = '123e4567-e89b-12d3-a456-426614174000'
    calendar_note_id = CalendarNoteID(value)
    assert calendar_note_id.value == value


def test_calendar_note_id_generate_should_create_instance() -> None:
    calendar_note_id = CalendarNoteID.generate()
    assert isinstance(calendar_note_id, CalendarNoteID)
    assert calendar_note_id.value is not None


def test_calendar_note_id_str_should_return_string_representation() -> None:
    value = '123e4567-e89b-12d3-a456-426614174000'
    calendar_note_id = CalendarNoteID(value)
    assert str(calendar_note_id) == value


# Title
@pytest.mark.parametrize(
    'title',
    ['The Prom Night', 'The Professor Breena Speach', 'The Veyran presentation'],
)
def test_calendar_note_title_constructor_should_create_instance(title: str) -> None:
    calendar_note_title = CalendarNoteTitle(title)
    assert calendar_note_title.value == title


@pytest.mark.parametrize(
    'title',
    ['', 'A', 'Invalid@Title', 'X' * 101],
    ids=['empty', 'too_short', 'invalid_chars', 'too_long'],
)
def test_calendar_note_title_constructor_should_raise_exception(title: str) -> None:
    with pytest.raises(CalendarNoteInvalidTitleException):
        CalendarNoteTitle(title)


# Description
@pytest.mark.parametrize(
    'description',
    ['This is a valid description.' * 1, 'A' * 5000],
    ids=['valid_description', 'max_length_description'],
)
def test_calendar_note_description_constructor_should_create_instance(description: str) -> None:
    calendar_note_description = CalendarNoteDescription(description)
    assert calendar_note_description.value == description


@pytest.mark.parametrize(
    'description', ['', 'Too short', 'A' * 5001], ids=['empty', 'too_short', 'too_long']
)
def test_calendar_note_description_constructor_should_raise_exception(description: str) -> None:
    with pytest.raises(CalendarNoteInvalidDescriptionException):
        CalendarNoteDescription(description)


# GameDatetime
@pytest.mark.parametrize(
    'game_datetime', ['2024-12-01T12:30:00Z', '2023-12-21T12:30:00Z', '2027-04-30T12:30:00Z']
)
def test_calendar_note_game_datetime_constructor_should_create_instance(game_datetime: str) -> None:
    game_datetime = datetime.fromisoformat(game_datetime.replace('Z', '+00:00'))
    calendar_note_game_datetime = CalendarNoteGameDatetime(game_datetime)
    assert calendar_note_game_datetime.value == game_datetime


@pytest.mark.parametrize(
    'game_datetime',
    ['', 'A', 'Invalid#GameDatetime', 'X' * 101, '2025-12-40T12:30:00Z', '2025-15-01T12:30:00Z'],
    ids=['empty', 'too_short', 'invalid_chars', 'too_long', 'invalid_day', 'invalid_month'],
)
def test_calendar_note_game_datetime_constructor_should_raise_exception(game_datetime: str) -> None:
    with pytest.raises(CalendarNoteInvalidDatetimeException):
        CalendarNoteGameDatetime(game_datetime)


# Is Exam
@pytest.mark.parametrize('is_exam', [True, False])
def test_calendar_note_is_exam_constructor_should_create_instance(is_exam: bool) -> None:
    calendar_note_exam = CalendarNoteIsExam(is_exam)
    assert calendar_note_exam.value is is_exam


@pytest.mark.parametrize('is_exam', ['true', 1, None])
def test_calendar_note_is_exam_constructor_should_raise_exception(is_exam: bool) -> None:
    with pytest.raises(CalendarNoteInvalidIsExamException):
        CalendarNoteIsExam(is_exam)
