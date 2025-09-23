from sqlalchemy import extract
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import delete, select

from src.modules.calendar_events.entity import CalendarNote
from src.modules.calendar_events.model import CalendarNoteModel


class CalendarNoteRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, calendar_note: CalendarNote) -> None:
        calendar_note_model = CalendarNoteModel.from_entity(calendar_note)
        self.session.add(calendar_note_model)
        await self.session.commit()

    async def update(self, calendar_note: CalendarNote) -> None:
        query = select(CalendarNoteModel).where(CalendarNoteModel.external_id == calendar_note.id)
        result = await self.session.execute(query)
        calendar_note_model = result.scalars().one()
        calendar_note_model.title = calendar_note.title
        calendar_note_model.description = calendar_note.description
        calendar_note_model.game_datetime = calendar_note.game_datetime
        calendar_note_model.is_exam = calendar_note.is_exam
        await self.session.commit()

    async def delete(self, calendar_note: CalendarNote) -> None:
        query = delete(CalendarNoteModel).where(CalendarNoteModel.external_id == calendar_note.id)
        await self.session.execute(query)
        await self.session.commit()

    async def find(self, calendar_note_id: str) -> CalendarNote | None:
        if calendar_note_id:
            query = select(CalendarNoteModel).where(CalendarNoteModel.external_id == calendar_note_id)

        try:
            result = await self.session.execute(query)
            calendar_note_model = result.scalars().one()
            return calendar_note_model.to_entity()
        except NoResultFound:
            return None

    async def find_by_game_month(self, calendar_month: int) -> list[CalendarNote] | None:
        if calendar_month:
            query = select(CalendarNoteModel).where(
                extract('month', CalendarNoteModel.game_datetime) == calendar_month
            )

        try:
            result = await self.session.execute(query)
            calendar_note_models = result.scalars().all()
            return [calendar_note_model.to_entity() for calendar_note_model in calendar_note_models]
        except NoResultFound:
            return None

    async def find_all(self) -> list[CalendarNote] | None:
        query = select(CalendarNoteModel)
        result = await self.session.execute(query)
        calendar_note_models = result.scalars().all()
        return [calendar_note_model.to_entity() for calendar_note_model in calendar_note_models]
