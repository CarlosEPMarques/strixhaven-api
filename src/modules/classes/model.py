from __future__ import annotations
from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime as DateTimeType
from sqlalchemy.types import String, Text

from src.modules.classes.entity import Class
from src.modules.classes.value_object import ClassCollegeID, ClassDescription, ClassID, ClassImageUrl, ClassName
from src.settings.database.sqlalchemy import Base
from src.utils.value_object import DateTime
from src.modules.college.college_model import CollegeModel

class ClassModel(Base):
    __tablename__ = "classes"

    internal_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    college_id: Mapped[int] = mapped_column(
        ForeignKey("colleges.internal_id", ondelete="SET NULL"),
        nullable=True,
    )
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTimeType(timezone=True), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTimeType(timezone=True), nullable=False
    )

    def to_entity(self) -> Class:
        return Class(
            id=ClassID(str(self.external_id)),
            name=ClassName(self.name),
            description=ClassDescription(self.description),
            college_id=ClassCollegeID(self.college_id),
            image_url=ClassImageUrl(self.image_url),
            created_at=DateTime(self.created_at),
            updated_at=DateTime(self.updated_at)
        )
    
    @staticmethod
    def from_entity(_class: Class) -> ClassModel:
        return ClassModel(
            external_id=_class.id,
            name=_class.name,
            description=_class.description,
            college_id=_class.college_id,
            image_url=_class.image_url,
            created_at=_class.created_at,
            updated_at=_class.updated_at
        )

    def __repr__(self):
        return f'ClassModel(id={self.external_id}, name={self.name}, description={self.description}, college_id={self.college_id})' # noqa: E501