from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import text, ForeignKey
from src.settings.database.sqlalchemy import Base


class CollegeModel(Base):
    __tablename__ = "colleges"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
