from __future__ import annotations

from pydantic import BaseModel, Field

from src.modules.book.entity import Book
from src.modules.book.value_object import (
    BookImageUrl,
    BookIsHidden,
    BookSection,
    BookSummary,
    BookTitle,
)


class BookCreateInput(BaseModel):
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(
        examples=[
            'In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'  # noqa: E501
        ]
    )
    section: str = Field(examples=['Fantasy'])
    is_hidden: bool = Field(examples=[False])
    image_url: str = Field(examples=['https://lordoftherings-image.com'])

    def to_entity(self) -> Book:
        return Book.create(
            title=BookTitle(self.title),
            summary=BookSummary(self.summary),
            section=BookSection(self.section),
            is_hidden=BookIsHidden(self.is_hidden),
            image_url=BookImageUrl(self.image_url),
        )


class BookUpdateInput(BaseModel):
    title: str | None = Field(default=None, examples=['The Lord of The Rings'])
    summary: str | None = Field(
        default=None,
        examples=[
            'In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'  # noqa: E501
        ],
    )
    section: str | None = Field(default=None, examples=['Fantasy'])
    is_hidden: bool | None = Field(default=None, examples=[False])
    image_url: str | None = Field(default=None, examples=['https://lordoftherings-image.com'])


class BookOutput(BaseModel):
    id: str = Field(examples=['casQJWEqkohQE5643HRcmxnRT'])
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(
        examples=[
            'In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'  # noqa: E501
        ]
    )
    section: str = Field(examples=['Fantasy'])
    is_hidden: bool = Field(examples=[False])
    image_url: str = Field(examples=['https://lordoftherings-image.com'])

    @staticmethod
    def from_entity(book: Book) -> BookOutput:
        return BookOutput(
            id=book.id,
            title=book.title,
            summary=book.summary,
            section=book.section,
            is_hidden=book.is_hidden,
            image_url=book.image_url,
        )
