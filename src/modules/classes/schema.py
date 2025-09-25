from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from src.modules.classes.entity import Class
from src.modules.classes.value_object import (
    ClassName,
    ClassDescription,
    ClassImageUrl,
    ClassCollegeID,
)


class ClassCreateInput(BaseModel):
    name: str = Field(examples=["The History behind the artifacts I"])
    description: str = Field(
        examples=[
            "In this class, you will learn how small objects tell the best histories."
        ]
    )
    college_id: int = Field(examples=[1])
    image_url: str = Field(examples=["https://artifacts.com.br/images"])

    def to_entity(self) -> Class:
        return Class.create(
            name=ClassName(self.name),
            description=ClassDescription(self.description),
            college_id=ClassCollegeID(self.college_id),
            image_url=ClassImageUrl(self.image_url),
        )


class ClassUpdateInput(BaseModel):
    name: str | None = Field(
        default=None, examples=["The History behind the artifacts I"]
    )
    description: str | None = Field(
        default=None,
        examples=[
            "In this class, you will learn how small objects tell the best histories."
        ],
    )
    college_id: int | None = Field(default=None, examples=[1])
    image_url: str | None = Field(
        default=None, examples=["https://artifacts.com.br/images"]
    )


class ClassOutput(BaseModel):
    id: str = Field(examples=["cPi23fsoIPVUmkL"])
    name: str = Field(examples=["The History behind the artifacts I"])
    description: str = Field(
        examples=[
            "In this class, you will learn how small objects tell the best histories."
        ]
    )
    college_id: int = Field(examples=[1])
    image_url: str = Field(examples=["https://artifacts.com.br/images"])
    created_at: datetime = Field(examples=["2025-09-12T12:00:00Z"])
    updated_at: datetime = Field(examples=["2025-09-12T12:00:00Z"])

    @staticmethod
    def from_entity(_class: Class) -> ClassOutput:
        return ClassOutput(
            id=_class.external_id,
            name=_class.name,
            description=_class.description,
            college_id=_class.college_id,
            image_url=_class.image_url,
            created_at=_class.created_at,
            updated_at=_class.updated_at,
        )


class ClassesInput(BaseModel):
    page: int = Field(
        default=10, ge=1, le=100, description="Max number of items to return (1-100)"
    )
    size: int = Field(
        default=0,
        ge=0,
        description="Number of items to skip (0 = start from beginning)",
    )


class ClassesOutput(BaseModel):
    total: int = Field(examples=[50])
    page: int = Field(examples=[1])
    size: int = Field(examples=[2])
    pages: int = Field(examples=[25])
    classes: list[ClassOutput]
