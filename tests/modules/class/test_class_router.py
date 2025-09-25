from httpx import AsyncClient
from starlette import status
from src.modules.classes.entity import Class

async def test_crud_class(client: AsyncClient, class_entity: Class) -> None:
    # Create
    response = await client.post(
        '/classes', json={
            'name': class_entity.name,
            'description': class_entity.description,
            'college_id': class_entity.college_id,
            'image_url': class_entity.image_url
        }
    )
    output = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert output['id'] is not None
    assert output['name'] == class_entity.name
    assert output['description'] == class_entity.description
    assert output['college_id'] == class_entity.college_id
    assert output['image_url'] == class_entity.image_url

    # Read
    response = await client.get(f'/classes/{output["id"]}')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert output['name'] == class_entity.name
    assert output['description'] == class_entity.description
    assert output['college_id'] == class_entity.college_id
    assert output['image_url'] == class_entity.image_url

    # Update
    updated_name = 'Excavation II'
    response = await client.put(f'/classes/{output["id"]}', json={'name': updated_name})
    output = response.json()

    assert response.status_code == status.HTTP_202_ACCEPTED
    assert output['name'] == updated_name
    assert output['description'] == class_entity.description
    assert output['college_id'] == class_entity.college_id
    assert output['image_url'] == class_entity.image_url

    # Delete
    response = await client.delete(f'/classes/{output['id']}')
    assert response.status_code == status.HTTP_204_NO_CONTENT

async def test_get_classes(
    client: AsyncClient,
    class_entity: Class,
    class_entity_2: Class
) -> None:
    response = await client.get('/classes?page=10&size=1')
    output = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert output['classes'][0]['id'] == class_entity.id
    assert output['classes'][1]['id'] == class_entity_2.id