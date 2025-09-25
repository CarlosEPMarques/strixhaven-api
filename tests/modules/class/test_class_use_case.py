from unittest.mock import AsyncMock

import pytest

from src.modules.classes.entity import Class
from src.modules.classes.exception import ClassNotFoundException, ClassesNotFoundException
from src.modules.classes.repository import ClassRepository
from src.modules.classes.schema import ClassCreateInput, ClassOutput, ClassUpdateInput, ClassesInput
from src.modules.classes.usecase import ClassUseCase

async def test_create_class_usecase(
    class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository
) -> None:
    class_repository.find_by_name = AsyncMock(return_value=None)
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.create = AsyncMock()
    input_data = ClassCreateInput(
        name=class_entity.name,
        description=class_entity.description,
        college_id=class_entity.college_id,
        image_url=class_entity.image_url,
    )
    created_class = await class_usecase.create_class(input_data)
    assert created_class.id == class_entity.id

async def test_update_class_name_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.update = AsyncMock()
    update_class_name = 'Excavation II'
    updated_class = await class_usecase.update_class(
        class_id=class_entity.id, input_data=ClassUpdateInput(name=update_class_name)
    )

    assert updated_class.name == update_class_name


async def test_update_class_description_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.update = AsyncMock()
    update_class_description = 'Learn how the artifacts tell stories about the ancient times.'
    updated_class = await class_usecase.update_class(
        class_id=class_entity.id, input_data=ClassUpdateInput(description=update_class_description)
    )

    assert updated_class.description == update_class_description


async def test_update_class_college_id_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.update = AsyncMock()
    update_class_college_id = 2
    updated_class = await class_usecase.update_class(
        class_id=class_entity.id, input_data=ClassUpdateInput(college_id=update_class_college_id)
    )

    assert updated_class.college_id == update_class_college_id


async def test_update_class_image_url_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.update = AsyncMock()
    update_class_image_url = 'https://strixhaven.com/lorehold-classes/15'
    updated_class = await class_usecase.update_class(
        class_id=class_entity.id, input_data=ClassUpdateInput(image_url=update_class_image_url)
    )

    assert updated_class.image_url == update_class_image_url


async def test_delete_class_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=class_entity)
    class_repository.update = AsyncMock()
    update_class_name = ''
    updated_class = await class_usecase.update_class(
        class_id=class_entity.id, input_data=ClassUpdateInput(name=update_class_name)
    )

    assert updated_class.name == update_class_name


async def test_delete_class_usecase_not_found(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find = AsyncMock(return_value=None)

    with pytest.raises(ClassNotFoundException) as error:
        await class_usecase.update_class(class_id='random-id', input_data=ClassUpdateInput())

    assert str(error.value) == ClassNotFoundException.detail


async def test_find_class_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find = AsyncMock(return_value=class_entity)
    result = await class_usecase.find_class(class_entity.id)

    assert result == ClassOutput.from_entity(class_entity)


async def test_find_class_usecase_not_found(class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_by_id = AsyncMock(return_value=None)

    with pytest.raises(ClassNotFoundException) as error:
        await class_usecase.find_class_by_id('non-existent-id')

    assert str(error.value) == ClassNotFoundException.detail


async def test_find_classes_usecase(class_entity: Class, class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_all_ids = AsyncMock(return_value=[class_entity.id])
    class_repository.find_all_paginated = AsyncMock(return_value=[class_entity])
    input_data = ClassesInput(size=0, page=10)
    output = await class_usecase.find_classes(input_data)

    assert output.total == 1
    assert output.page == 0
    assert output.size == 10  # noqa: PLR2004
    assert output.pages == 1


async def test_find_classes_usecase_not_found(class_usecase: ClassUseCase, class_repository: ClassRepository) -> None:
    class_repository.find_all_paginated = AsyncMock(return_value=None)
    input_data = ClassesInput(size=0, page=10)

    with pytest.raises(ClassesNotFoundException) as error:
        await class_usecase.find_classes(input_data)

    assert str(error.value) == ClassesNotFoundException.detail

