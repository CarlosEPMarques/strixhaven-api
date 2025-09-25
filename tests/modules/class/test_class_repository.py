from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.classes.entity import Class
from src.modules.classes.repository import ClassRepository
from src.modules.classes.value_object import ClassName


async def test_crud_class(session: AsyncSession, class_entity: Class) -> None:
    class_repository = ClassRepository(session)

    # Create
    await class_repository.find_by_name(class_entity.name)
    await class_repository.create(class_entity)
    created_class = await class_repository.find_by_id(class_entity.id)
    assert created_class is not None

    # Read
    found_class = await class_repository.find_by_id(class_entity.id)
    assert found_class is not None
    assert found_class.name == class_entity.name

    # Update
    updated_name = 'Artifacts II'
    found_class.update_name(ClassName(updated_name))
    await class_repository.update(found_class)
    updated_class = await class_repository.find_by_id(found_class.id)
    assert updated_class.name == updated_name

    # Delete
    await class_repository.delete(updated_class)
    deleted_class = await class_repository.find_by_id(updated_class.id)
    assert deleted_class is None