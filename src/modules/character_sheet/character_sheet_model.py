from uuid import UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import text, ForeignKey, Integer, Float, Text, func
from src.settings.database.sqlalchemy import Base
from sqlalchemy.types import DateTime as DateTimeType


class CharacterSheetModel(Base):
    __tablename__ = "character_sheet"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    character_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("player_characters.id", ondelete="CASCADE"),
        nullable=False,
    )
    strength: Mapped[int] = mapped_column(Integer, nullable=True)
    dexterity: Mapped[int] = mapped_column(Integer, nullable=True)
    constitution: Mapped[int] = mapped_column(Integer, nullable=True)
    intelligence: Mapped[int] = mapped_column(Integer, nullable=True)
    wisdom: Mapped[int] = mapped_column(Integer, nullable=True)
    charisma: Mapped[int] = mapped_column(Integer, nullable=True)
    proficiency_bonus: Mapped[int] = mapped_column(Integer, nullable=True)
    armor_class: Mapped[int] = mapped_column(Integer, nullable=True)
    initiative: Mapped[int] = mapped_column(Integer, nullable=True)
    speed: Mapped[float] = mapped_column(Float, nullable=True)
    max_hit_points: Mapped[int] = mapped_column(Integer, nullable=True)
    current_hit_points: Mapped[int] = mapped_column(Integer, nullable=True)
    temp_hit_points: Mapped[int] = mapped_column(Integer, nullable=True)
    hit_dice_total: Mapped[int] = mapped_column(Integer, nullable=True)
    hit_dice_current: Mapped[int] = mapped_column(Integer, nullable=True)
    save_str: Mapped[int] = mapped_column(Integer, nullable=True)
    save_dex: Mapped[int] = mapped_column(Integer, nullable=True)
    save_con: Mapped[int] = mapped_column(Integer, nullable=True)
    save_int: Mapped[int] = mapped_column(Integer, nullable=True)
    save_wis: Mapped[int] = mapped_column(Integer, nullable=True)
    save_cha: Mapped[int] = mapped_column(Integer, nullable=True)
    skills: Mapped[str] = mapped_column(Text, nullable=True)
    background: Mapped[str] = mapped_column(Text, nullable=True)
    race: Mapped[str] = mapped_column(Text, nullable=True)
    alignment: Mapped[str] = mapped_column(Text, nullable=True)
    experience_points: Mapped[int] = mapped_column(Integer, nullable=True)
    languages: Mapped[str] = mapped_column(Text, nullable=True)
    features_traits: Mapped[str] = mapped_column(Text, nullable=True)
    proficiencies: Mapped[str] = mapped_column(Text, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTimeType(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTimeType(timezone=True), server_default=func.now(), onupdate=func.now()
    )
