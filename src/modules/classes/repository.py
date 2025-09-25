from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import delete, select

from src.modules.classes.entity import Class
from src.modules.classes.model import ClassModel

class ClassRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, _class: Class) -> None:
        class_model = ClassModel.from_entity(_class)
        self.session.add(class_model)
        await self.session.commit()

    async def update(self, _class: Class) -> None:
        class_model = ClassModel.from_entity(_class)
        await self.session.merge(class_model)
        await self.session.commit()

    async def delete(self, _class: Class) -> None:
        query = delete(ClassModel).where(ClassModel.external_id == _class.external_id)
        await self.session.execute(query)
        await self.session.commit()

    async def find_by_id(self, class_id: str) -> Class | None:
        query = select(ClassModel).where(ClassModel.external_id == class_id)
        try:
            result = await self.session.execute(query)
            class_model = result.scalars().one()
            return class_model.to_entity()
        except NoResultFound:
            return None
        
    async def find_by_name(self, class_name: str) -> Class | None:
        query = select(ClassModel).where(ClassModel.name == class_name)
        try:
            result = await self.session.execute(query)
            class_model = result.scalars().one()
            return class_model.to_entity()
        except NoResultFound:
            return None
        
    async def find_by_college_id(self, college_id: str) -> list[Class] | None:
        query = select(ClassModel).where(ClassModel.college_id == college_id)
        result = await self.session.execute(query)
        class_models = result.scalars().all()
        return [class_model.to_entity() for class_model in class_models]
    
    async def find_all_paginated(self, page: int, size: int) -> list[Class]:
        query = select(ClassModel).offset((size - 1) * page).limit(page)
        result = await self.session.execute(query)
        class_models = result.scalars().all()
        return [class_model.to_entity() for class_model in class_models]
    
    async def find_all_ids(self) -> list[str]:
        query = select(ClassModel.external_id)
        result = await self.session.execute(query)
        classes_models = result.scalars().all()
        return [class_model[0] for class_model in classes_models]