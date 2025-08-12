from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey
from src.settings.database.sqlalchemy import Base

class CharacterNoteModel(Base):
    __tablename__ = "character_notes"

    note_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("notes.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )
    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("player_characters.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )
