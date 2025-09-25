from math import ceil
from typing import cast

from src.modules.classes.entity import Class
from src.modules.classes.exception import (

    ClassAlreadyExistsException,
    ClassNotFoundException,
    ClassesNotFoundException,
)
from src.modules.classes.repository import ClassRepository
from src.modules.classes.schema import (
    ClassCreateInput,
    ClassOutput,
    ClassUpdateInput,
    ClassesInput,
    ClassesOutput,
)
from src.modules.classes.value_object import (
    ClassName,
    ClassDescription,
    ClassCollegeID,
    ClassImageUrl,
)


class ClassUseCase:
    def __init__(self, class_repository: ClassRepository) -> None:
        self.class_repository = class_repository

    async def create_class(self, input_data: ClassCreateInput) -> ClassOutput:
        existing_class = await self.class_repository.find_by_name(input_data.name)
        if existing_class:
            raise ClassAlreadyExistsException(input_data.name)
        _class = input_data.to_entity()
        await self.class_repository.create(_class)
        created_class = await self.class_repository.find_by_name(_class.name)
        return ClassOutput.from_entity(cast(Class, created_class))
    
    async def update_class(self, class_id: str, input_data: ClassUpdateInput) -> ClassOutput:
        _class = await self.class_repository.find_by_id(class_id)
        if not _class:
            raise ClassNotFoundException
        if input_data.name:
            _class.update_name(ClassName(input_data.name))
        if input_data.description:
            _class.update_description(ClassDescription(input_data.description))
        if input_data.college_id:
            _class.update_college_id(ClassCollegeID(input_data.college_id))
        if input_data.image_url:
            _class.update_image_url(ClassImageUrl(input_data.image_url))
        await self.class_repository.update(_class)
        updated_class = await self.class_repository.find_by_id(
            class_id=_class.external_id
        )
        return ClassOutput.from_entity(cast(Class, updated_class))
    
    async def delete_class(self, class_id: str) -> None:
        _class = await self.class_repository.find(class_id)
        if not _class:
            raise ClassNotFoundException
        await self.class_repository.delete(_class)

    async def find_class_by_id(self, class_id: str) -> ClassOutput:
        _class = await self.class_repository.find_by_id(class_id)
        if not _class:
            raise ClassNotFoundException
        return ClassOutput.from_entity(cast(Class, _class))
    
    async def find_classes(self, input_data: ClassesInput) -> ClassesOutput:
        classes = await self.class_repository.find_all_paginated(page=input_data.page, size=input_data.size)
        if not classes:
            raise ClassesNotFoundException
        total = len(await self.class_repository.find_all_ids())
        pages = ceil(total / input_data.page)
        classes_output = [ClassOutput.from_entity(_class) for _class in classes]
        return ClassesOutput(
            page=input_data.page,
            size=input_data.size,
            total=total,
            pages=pages,
            classes=classes_output
        )