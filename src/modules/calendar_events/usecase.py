from typing import cast

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
from src.modules.calendar_events.object import (
    CalendarNoteDescription,
    CalendarNoteGameDatetime,
    CalendarNoteIsExam,
    CalendarNoteTitle,
)


class CalendarNoteUseCase:
    def __init__(self, calendar_note_repository: CalendarNoteRepository) -> None:
        self.calendar_note_repository = calendar_note_repository

    async def create_calendar_note(self, input_data: CalendarNoteCreateInput) -> CalendarNoteOutput:
        calendar_note = input_data.to_entity()
        await self.calendar_note_repository.create(calendar_note)
        created_calendar_note = await self.calendar_note_repository.find(
            calendar_note_id=calendar_note.id
        )
        return CalendarNoteOutput.from_entity(cast(CalendarNote, created_calendar_note))

    async def update_calendar_note(
        self, calendar_note_id: str, input_data: CalendarNoteUpdateInput
    ) -> CalendarNoteOutput:
        calendar_note = await self.calendar_note_repository.find(calendar_note_id=calendar_note_id)
        if not calendar_note:
            raise CalendarNoteNotFoundException
        if input_data.title:
            calendar_note.update_title(CalendarNoteTitle(input_data.title))
        if input_data.description:
            calendar_note.update_description(CalendarNoteDescription(input_data.description))
        if input_data.game_datetime:
            calendar_note.update_game_datetime(CalendarNoteGameDatetime(input_data.game_datetime))
        if input_data.is_exam is not None:
            calendar_note.update_is_exam(CalendarNoteIsExam(input_data.is_exam))
        await self.calendar_note_repository.update(calendar_note)
        updated_calendar_note = await self.calendar_note_repository.find(
            calendar_note_id=calendar_note.id
        )
        return CalendarNoteOutput.from_entity(cast(CalendarNote, updated_calendar_note))

    async def delete_calendar_note(self, calendar_note_id: str) -> None:
        calendar_note = await self.calendar_note_repository.find(calendar_note_id=calendar_note_id)
        if not calendar_note:
            raise CalendarNoteNotFoundException
        await self.calendar_note_repository.delete(calendar_note)

    async def find_calendar_note_by_id(self, calendar_note_id: str) -> CalendarNoteOutput:
        calendar_note = await self.calendar_note_repository.find(calendar_note_id=calendar_note_id)
        if not calendar_note:
            raise CalendarNoteNotFoundException
        return CalendarNoteOutput.from_entity(cast(CalendarNote, calendar_note))

    async def find_calendar_note_by_month(self, calendar_month: int) -> list[CalendarNoteOutput]:
        calendar_notes = await self.calendar_note_repository.find_by_game_month(
            calendar_month=calendar_month
        )
        if not calendar_notes:
            raise CalendarNoteNotFoundException
        return [CalendarNoteOutput.from_entity(calendar_note) for calendar_note in calendar_notes]

    async def find_calendar_notes(self) -> list[CalendarNoteOutput]:
        calendar_notes = await self.calendar_note_repository.find_all()
        if not calendar_notes:
            raise CalendarNotesNotFoundException
        return [CalendarNoteOutput.from_entity(calendar_note) for calendar_note in calendar_notes]
