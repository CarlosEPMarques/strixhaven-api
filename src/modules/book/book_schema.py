from __future__ import annotations
from pydantic import BaseModel, Field
from src.modules.book.book_entity import Book
from src.modules.book.book_value_object import (BookTitle)

class BookCreateInput(BaseModel):
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(examples=['''
        In an age long past, in a corner of the world that men seldom visit, there lived a quiet and unassuming people called Hobbits.
    '''])
    section: str = Field(examples=['Fantasy'])
    is_hidden: bool = Field(examples=[False])
    image_url: str = Field(examples=['https://lordoftherings-image.com'])
    
    def to_entity(self) -> Book:
        return Book.create(
            title=Book(self.title),
            summary=Book(self.summary),
            section=Book(self.section),
            is_hidden=Book(self.is_hidden),
            image_url=Book(self.image_url),
        )
        
class BookUpdateInput(BaseModel):
    title: str | None = Field(default=None, examples=['The Lord of The Rings'])
    summary: str | None = Field(default=None, examples=['''
        In an age long past, in a corner of the world that men seldom visit, there lived a quiet and unassuming people called Hobbits.
    '''])
    section: str | None = Field(default=None, examples=['Fantasy'])
    is_hidden: bool | None = Field(default=None, examples=[False])
    image_url: str | None = Field(default=None, examples=['https://lordoftherings-image.com'])
    
class BookOutput(BaseModel):
    title: str = Field(examples=['The Lord of The Rings'])
    summary: str = Field(examples=['''
        In an age long past, in a corner of the world that men seldom visit, there lived a quiet and unassuming people called Hobbits.
    '''])
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
            image_url=book.image_url
        )
