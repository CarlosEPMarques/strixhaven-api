from __future__ import annotations
import uuid
from asyncpg.pgproto import pgproto

from .book_value_object import (
    BookID,
    BookTitle,
    BookSummary,
    BookSection,
    BookIsHidden,
    BookImageUrl,
)


class Book:
    def __init__(
        self,
        id: BookID,
        title: BookTitle,
        summary: BookSummary,
        section: BookSection,
        is_hidden: BookIsHidden,
        image_url: BookImageUrl,
    ) -> None:
        self._id = id
        self._title = title
        self._summary = summary
        self._section = section
        self._is_hidden = is_hidden
        self._image_url = image_url

    @property
    def id(self) -> str:
        if isinstance(self._id, uuid.UUID):
            return str(self._id)
        if isinstance(self._id, pgproto.UUID):
            return self._id.hex
        return str(self._id)

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def summary(self) -> str:
        return self._summary.value

    @property
    def section(self) -> str:
        return self._section.value

    @property
    def is_hidden(self) -> str:
        return self._is_hidden.value

    @property
    def image_url(self) -> str:
        return self._image_url.value

    def update_title(self, new_title) -> None:
        self._title = new_title

    def update_summary(self, new_summary) -> None:
        self._summary = new_summary

    def update_section(self, new_section) -> None:
        self._section = new_section

    def update_is_hidden(self, new_is_hidden) -> None:
        self._is_hidden = new_is_hidden

    def update_image_url(self, new_image_url) -> None:
        self._image_url = new_image_url

    def to_document(self) -> dict:
        return {
            '_id': self.id,
            'title': self.title,
            'summary': self.summary,
            'section': self.section,
            'is_hidden': self.is_hidden,
            'image_url': self.image_url
        }
        
    @staticmethod
    def from_document(document: dict) -> Book:
        return Book(
            id=BookID(document['_id']),
            title=BookTitle(document['title']),
            summary=BookSummary(document['summary']),
            section=BookSection(document['section']),
            is_hidden=BookIsHidden(document['is_hidden']),
            image_url=BookImageUrl(document['image_url']),
        )
        
    @staticmethod
    def create(
        title: BookTitle,
        summary: BookSummary,
        section: BookSection,
        is_hidden: BookIsHidden,
        image_url: BookImageUrl,
    ) -> Book:
        return Book(
            id=BookID.generate(),
            title=title,
            summary=summary,
            section=section,
            is_hidden=is_hidden,
            image_url=image_url,
        )