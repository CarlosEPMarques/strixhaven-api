from typing import Annotated

from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from starlette import status

from src.modules.classes.schema import (
    ClassesInput,
    ClassesOutput,
    ClassCreateInput,
    ClassOutput,
    ClassUpdateInput,
)
from src.modules.classes.usecase import ClassUseCase
from src.modules.classes.injection import class_usecase_factory

router = APIRouter(prefix='/classes', tags=['Classes'])

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_class(
    input_data: ClassCreateInput,
    usecase: Annotated[ClassUseCase, Depends(class_usecase_factory)]
) -> ClassOutput:
    return await usecase.create_class(input_data=input_data)

@router.get('', status_code=status.HTTP_200_OK)
async def get_classes(
    usecase: Annotated[ClassUseCase, Depends(class_usecase_factory)],
    input_data: ClassesInput = Depends()
) -> ClassesOutput:
    return await usecase.find_classes(input_data)

@router.get('{class_id}', status_code=status.HTTP_200_OK)
async def get_class(
    class_id: str, usecase: Annotated[ClassUseCase, Depends(class_usecase_factory)]
) -> ClassOutput:
    return await usecase.find_class_by_id(class_id)

@router.put('{class_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_class(
    class_id: str,
    input_data: ClassUpdateInput,
    usecase: Annotated[ClassUseCase, Depends(class_usecase_factory)]
) -> ClassOutput:
    return await usecase.update_class(class_id=class_id, input_data=input_data)

@router.delete('/{class_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(
    class_id: str, usecase: Annotated[ClassUseCase, Depends(class_usecase_factory)]
) -> None:
    return await usecase.delete_class(class_id)