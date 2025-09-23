from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.model import CalendarNoteModel


def test_calendar_note_model_from_entity(calendar_note: CalendarNote) -> None:
    calendar_note_model = CalendarNoteModel.from_entity(calendar_note)

    assert calendar_note_model.external_id == calendar_note.id
    assert calendar_note_model.title == calendar_note.title
    assert calendar_note_model.description == calendar_note.description
    assert calendar_note_model.game_datetime == calendar_note.game_datetime
    assert calendar_note_model.is_exam == calendar_note.is_exam


def test_calendar_note_model_to_entity(calendar_note: CalendarNote) -> None:
    calendar_note_model = CalendarNoteModel.from_entity(calendar_note)
    entity = calendar_note_model.to_entity()

    assert entity.id == calendar_note.id
    assert entity.title == calendar_note.title
    assert entity.description == calendar_note.description
    assert entity.game_datetime == calendar_note.game_datetime
    assert entity.is_exam == calendar_note.is_exam
