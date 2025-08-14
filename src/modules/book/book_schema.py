from __future__ import annotations
from pydantic import BaseModel, Field
from src.modules.book.book_entity import Book
from src.modules.book.book_value_object import (BookImageUrl, BookIsHidden, BookSection, BookSummary, BookTitle)

class BookCreateInput(BaseModel):
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(examples=['In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'])
    section: str = Field(examples=['Fantasy'])
    is_hidden: bool = Field(examples=[False])
    image_url: str = Field(examples=['https://lordoftherings-image.com'])
    
    def to_entity(self) -> Book:
        return Book.create(
            title=BookTitle(self.title).value,
            summary=BookSummary(self.summary).value,
            section=BookSection(self.section).value,
            is_hidden=BookIsHidden(self.is_hidden).value,
            image_url=BookImageUrl(self.image_url).value,
        )
        
class BookUpdateInput(BaseModel):
    title: str | None = Field(default=None, examples=['The Lord of The Rings'])
    summary: str = Field(examples=['In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'])
    section: str | None = Field(default=None, examples=['Fantasy'])
    is_hidden: bool | None = Field(default=None, examples=[False])
    image_url: str | None = Field(default=None, examples=['https://lordoftherings-image.com'])
    
class BookOutput(BaseModel):
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(examples=['In an age long past, in a corner of the world, there lived a quiet people called Hobbits.'])
    section: str = Field(examples=['Fantasy'])
    is_hidden: bool = Field(examples=[False])
    image_url: str = Field(examples=['https://lordoftherings-image.com'])
    
    @staticmethod
    def from_entity(book: Book) -> BookOutput:
        return BookOutput(
            id=book.id,
            title=book.title.value,
            summary=book.summary.value,
            section=book.section.value,
            is_hidden=book.is_hidden.value,
            image_url=book.image_url.value
        )
