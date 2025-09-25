from src.modules.classes.entity import Class
from src.modules.classes.model import ClassModel

def test_class_model_from_entity(class_entity: Class) -> None:
    class_model = ClassModel.from_entity(class_entity)

    assert class_model.external_id == class_entity.id
    assert class_model.name == class_entity.name
    assert class_model.description == class_entity.description
    assert class_model.college_id == class_entity.college_id
    assert class_model.image_url == class_entity.image_url

def test_class_model_to_entity(class_entity: Class) -> None:
    class_model = ClassModel.from_entity(class_entity)
    entity = class_model.to_entity()

    assert entity.id == class_entity.id
    assert entity.name == class_entity.name
    assert entity.description == class_entity.description
    assert entity.college_id == class_entity.college_id
    assert entity.image_url == class_entity.image_url
    assert entity.created_at == class_entity.created_at
    assert entity.updated_at == class_entity.updated_at

def test_class_model_repr(class_entity: Class) -> None:
    class_model = ClassModel.from_entity(class_entity)
    expected_repr = f'ClassModel(id={class_model.external_id}, name={class_model.name}, description={class_model.description}, college_id={class_model.college_id})'  # noqa: E501

    assert repr(class_model) == expected_repr