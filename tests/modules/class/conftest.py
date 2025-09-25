import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.classes.entity import Class
from src.modules.classes.repository import ClassRepository
from src.modules.classes.usecase import ClassUseCase
from src.modules.classes.value_object import (
    ClassName,
    ClassDescription,
    ClassCollegeID,
    ClassImageUrl,
)


@pytest.fixture
def class_entity() -> Class:
    class_name=ClassName('Excavation I')
    class_description=ClassDescription('Learn how the technics to excavate ancient tombs, and find treasures.')
    class_college_id=ClassCollegeID(1)
    class_image_url=ClassImageUrl('https://strixhaven.com/lorehold-classes/1')
    return Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

@pytest.fixture
def class_entity_2() -> Class:
    class_name=ClassName("Nature's Mathematics I")
    class_description=ClassDescription('Mother Nature have many ways to teach us the true value behind the mathematics expressions.')
    class_college_id=ClassCollegeID(3)
    class_image_url=ClassImageUrl('https://strixhaven.com/quandrix-classes/1')
    return Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

@pytest.fixture
def class_repository(session: AsyncSession) -> ClassRepository:
    return ClassRepository(session=session)

@pytest.fixture
def class_usecase(class_repository: ClassRepository) -> ClassUseCase:
    return ClassUseCase(class_repository)