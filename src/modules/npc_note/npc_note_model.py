from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.settings.database.sqlalchemy import Base


class NPCNoteModel(Base):
    __tablename__ = 'npc_notes'

    note_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey('notes.id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
    )
    npc_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey('npcs.id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
    )
    author_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
