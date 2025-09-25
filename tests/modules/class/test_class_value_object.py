import pytest 
from src.modules.classes.exception import (
    ClassInvalidCollegeIdException,
    ClassInvalidDescriptionException,
    ClassInvalidImageUrlException,
    ClassInvalidNameException
)

from src.modules.classes.value_object import (
    ClassID,
    ClassName,
    ClassDescription,
    ClassCollegeID,
    ClassImageUrl
)

# ID
def test_class_id_constructor_should_create_instance() -> None:
    value = '123e4567-e89b-12d3-a456-426614174000'
    class_id = ClassID(value)
    assert class_id.value == value

def test_class_id_generate_should_create_instance() -> None:
    class_id = ClassID.generate()
    assert isinstance(class_id, ClassID)
    assert class_id.value is not None
def test_class_id_str_should_return_string_representation() -> None:
    value = '123e4567-e89b-12d3-a456-426614174000'
    class_id = ClassID(value)
    assert str(class_id) == value

# Title
@pytest.mark.parametrize(
    'name',
    ['Excavation', 'Mother Nature Mathematics', 'Dialogues Technics'],
)
def test_class_name_constructor_should_create_instance(name: str) -> None:
    class_name = ClassName(name)
    assert class_name.value == name


@pytest.mark.parametrize(
    'name',
    ['', 'A', 'Invalid@name', 'X' * 101],
    ids=['empty', 'too_short', 'invalid_chars', 'too_long'],
)
def test_class_name_constructor_should_raise_exception(name: str) -> None:
    with pytest.raises(ClassInvalidNameException):
        ClassName(name)

# Description
@pytest.mark.parametrize(
    'description',
    ['This is a valid description.' * 1, 'A' * 5000],
    ids=['valid_description', 'max_length_description'],
)
def test_class_description_constructor_should_create_instance(description: str) -> None:
    class_description = ClassDescription(description)
    assert class_description.value == description


@pytest.mark.parametrize(
    'description', ['', 'Too short', 'A' * 5001], ids=['empty', 'too_short', 'too_long']
)
def test_class_description_constructor_should_raise_exception(description: str) -> None:
    with pytest.raises(ClassInvalidDescriptionException):
        ClassDescription(description)

# College ID
@pytest.mark.parametrize('college_id', [1, 2, 3])
def test_class_college_id_constructor_should_create_instance(college_id: int) -> None:
    class_college_id = ClassCollegeID(college_id)
    assert class_college_id.value == college_id


@pytest.mark.parametrize(
    'college_id',
    ['', 'A', 'Invalid#collegeId', 'X' * 101],
    ids=['empty', 'too_short', 'invalid_chars', 'too_long'],
)
def test_class_college_id_constructor_should_raise_exception(college_id: int) -> None:
    with pytest.raises(ClassInvalidCollegeIdException):
        ClassCollegeID(college_id)

# Image URL
@pytest.mark.parametrize('url', ['http://example.com/image.png', 'https://example.com/img.jpg'])
def test_class_image_url_constructor_should_create_instance(url: str) -> None:
    class_image = ClassImageUrl(url)
    assert class_image.value == url


@pytest.mark.parametrize('url', ['ftp://example.com/image.png', 'example.com/img.jpg', '', None])
def test_class_image_url_constructor_should_raise_exception(url: str) -> None:
    with pytest.raises(ClassInvalidImageUrlException):
        ClassImageUrl(url)