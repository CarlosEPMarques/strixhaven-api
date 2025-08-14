from __future__ import annotations
from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, Text, Boolean
from sqlalchemy import text
from src.modules.book.book_entity import Book
from src.modules.book.book_value_object import (
    BookID,
    BookImageUrl, 
    BookIsHidden, 
    BookSection, 
    BookSummary, 
    BookTitle
)
from src.settings.database.sqlalchemy import Base

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(
        primary_key=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    section: Mapped[str] = mapped_column(String(255), nullable=True)
    is_hidden: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"), nullable=False)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)

    def to_entity(self) -> Book:
        return Book(
            id=BookID(str(self.id)),
            title=BookTitle(self.title),
            summary=BookSummary(self.summary),
            section=BookSection(self.section),
            is_hidden=BookIsHidden(self.is_hidden),
            image_url=BookImageUrl(self.image_url)
        )
        
    @staticmethod
    def from_entity(book: Book) -> BookModel:
        return BookModel(
            id=book.id,
            title=book.title,
            summary=book.summary,
            section=book.section,
            is_hidden=book.is_hidden,
            image_url=book.image_url
        )