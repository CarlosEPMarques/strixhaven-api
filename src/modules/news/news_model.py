from datetime import datetime
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime as DateTimeType
from sqlalchemy.types import String, Text

from src.settings.database.sqlalchemy import Base


class NewsModel(Base):
    __tablename__ = 'news'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()')
    )
    headline: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=True)
    game_datetime: Mapped[datetime] = mapped_column(DateTimeType(timezone=True), nullable=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
