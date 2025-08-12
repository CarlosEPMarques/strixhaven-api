from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.types import String, Integer, Text
from sqlalchemy import text
from src.settings.database.sqlalchemy import Base

class MonsterModel(Base):
    __tablename__ = "monsters"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    hit_points: Mapped[int] = mapped_column(Integer, nullable=True)
    experience_points: Mapped[int] = mapped_column(Integer, nullable=True)
    strength: Mapped[int] = mapped_column(Integer, nullable=True)
    dexterity: Mapped[int] = mapped_column(Integer, nullable=True)
    constitution: Mapped[int] = mapped_column(Integer, nullable=True)
    intelligence: Mapped[int] = mapped_column(Integer, nullable=True)
    wisdom: Mapped[int] = mapped_column(Integer, nullable=True)
    charisma: Mapped[int] = mapped_column(Integer, nullable=True)
    armor_class: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
