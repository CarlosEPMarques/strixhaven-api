from uuid import UUID

from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer

from src.settings.database.sqlalchemy import Base


class NPCReputationModel(Base):
    __tablename__ = 'npcs_reputation'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()')
    )
    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey('player_characters.id', ondelete='CASCADE'),
        nullable=False,
    )
    npc_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey('npcs.id', ondelete='CASCADE'), nullable=False
    )
    score: Mapped[int] = mapped_column(Integer, nullable=True)
