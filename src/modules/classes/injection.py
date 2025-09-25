from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.classes.repository import ClassRepository
from src.modules.classes.usecase import ClassUseCase
from src.settings.database.sqlalchemy.database import get_session


def class_usecase_factory(
    database: AsyncSession = Depends(get_session),
) -> ClassUseCase:
    class_repository = ClassRepository(database)
    return ClassUseCase(class_repository)
