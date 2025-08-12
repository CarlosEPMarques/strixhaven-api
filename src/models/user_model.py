from uuid import UUID
from src.models.user_role_enum import UserRole
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import ENUM, UUID as PG_UUID
from src.settings.database.sqlalchemy import Base
from sqlalchemy import text


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(
        ENUM(UserRole, name="user_role", create_type=False), nullable=False
    )
    avatar_url: Mapped[str] = mapped_column(Text, nullable=True)
