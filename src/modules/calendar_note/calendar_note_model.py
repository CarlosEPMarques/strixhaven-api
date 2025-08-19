from datetime import datetime
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, String, Text
from sqlalchemy.types import DateTime as DateTimeType

from src.settings.database.sqlalchemy import Base


class CalendarNoteModel(Base):
    __tablename__ = 'calendar_notes'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text('gen_random_uuid()'),
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    game_datetime: Mapped[datetime] = mapped_column(DateTimeType(timezone=True), nullable=True)
    is_exam: Mapped[bool] = mapped_column(Boolean, server_default=text('FALSE'), nullable=False)
