from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.types import String
from sqlalchemy.types import DateTime as DateTimeType
from sqlalchemy import func
from src.settings.database.sqlalchemy import Base

class SessionModel(Base):
    __tablename__ = "sessions"

    session_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        nullable=False
    )
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        nullable=False
    )
    created_at: Mapped = mapped_column(
        DateTimeType(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False
    )
    expires_at: Mapped = mapped_column(
        DateTimeType(timezone=True),
        nullable=False
    )
