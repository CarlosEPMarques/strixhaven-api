from __future__ import annotations
import uuid
from datetime import datetime
from asyncpg.pgproto import pgproto

from .value_object import (
    ClassID,
    ClassName,
    ClassDescription,
    ClassCollegeID,
    ClassImageUrl,
)
from src.utils import DateTime


class Class:
    def __init__(
        self,
        id: ClassID,
        name: ClassName,
        description: ClassDescription,
        college_id: ClassCollegeID,
        image_url: ClassImageUrl,
        created_at: DateTime,
        updated_at: DateTime,
    ) -> None:
        self._id = id
        self._name = name
        self._description = description
        self._college_id = college_id
        self._image_url = image_url
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> str:
        if isinstance(self._id, uuid.UUID):
            return str(self._id)
        if isinstance(self._id, pgproto.UUID):
            return self._id.hex
        return str(self._id)

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def college_id(self) -> int:
        return self._college_id.value

    @property
    def image_url(self) -> str:
        return self._image_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def update_name(self, new_name) -> None:
        self._name = new_name
        self._updated_at = DateTime.now()

    def update_description(self, new_description) -> None:
        self._description = new_description
        self._updated_at = DateTime.now()

    def update_college_id(self, new_college_id) -> None:
        self._college_id = new_college_id
        self._updated_at = DateTime.now()

    def update_image_url(self, new_image_url) -> None:
        self._image_url = new_image_url
        self._updated_at = DateTime.now()

    @staticmethod
    def from_document(document: dict) -> Class:
        return Class(
            id=ClassID(document['id']),
            name=ClassName(document['name']),
            description=ClassDescription(document['description']),
            college_id=ClassCollegeID(document['college_id']),
            image_url=ClassImageUrl(document['image_url']),
            created_at=DateTime(document['created_at']),
            updated_at=DateTime(document['updated_at']),
        )
    
    @staticmethod
    def create(name, description, college_id, image_url) -> Class:
        return Class(
            id=ClassID.generate(),
            name=name,
            description=description,
            college_id=college_id,
            image_url=image_url,
            created_at=DateTime.now(),
            updated_at=DateTime.now(),
        )
    
    def __repr__(self):
        return f'<Class {self.id} | {self.name}>'