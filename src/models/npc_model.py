from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.types import String, Text, Boolean
from sqlalchemy import text
from src.settings.database.sqlalchemy import Base


class NPCModel(Base):
    __tablename__ = "npcs"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    is_visible: Mapped[bool] = mapped_column(
        Boolean, server_default=text("TRUE"), nullable=False
    )
    visible_to: Mapped[str] = mapped_column(Text, nullable=True)
