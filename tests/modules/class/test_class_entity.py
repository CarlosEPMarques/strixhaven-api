from datetime import datetime

from src.modules.classes.entity import Class
from src.modules.classes.value_object import (
    ClassExternalID,
    ClassName,
    ClassDescription,
    ClassCollegeID,
    ClassImageUrl
)

def test_constructor_should_create_instance() -> None:
    class_name=ClassName('Dialogue Technics - I')
    class_description=ClassDescription('Learn how to convince your listeners by your best weapon, dialogues.')
    class_college_id=ClassCollegeID(2)
    class_image_url=ClassImageUrl('https://strixhaven.com/silverquill-classes/1')
    _class = Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

    assert _class.external_id is not None
    assert _class.created_at is not None
    assert _class.updated_at is not None
    assert _class.name == class_name.value
    assert _class.description == class_description.value
    assert _class.college_id == class_college_id.value
    assert _class.image_url == class_image_url.value
    assert repr(_class) == f'<Class {_class.external_id} | {class_name.value}>'

def test_update_class_name() -> None:
    class_name=ClassName('Dialogue Technics I')
    class_description=ClassDescription('Learn how to convince your listeners by your best weapon, dialogues.')
    class_college_id=ClassCollegeID(2)
    class_image_url=ClassImageUrl('https://strixhaven.com/silverquill-classes/1')
    _class = Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

    assert _class.name == class_name.value

    new_class_name = ClassName('Dialogue Technics II')
    _class.update_name(new_name=new_class_name)
    
    assert _class.name == new_class_name.value

def test_update_class_description() -> None:
    class_name=ClassName('Dialogue Technics I')
    class_description=ClassDescription('Learn how to convince your listeners by your best weapon, dialogues.')
    class_college_id=ClassCollegeID(2)
    class_image_url=ClassImageUrl('https://strixhaven.com/silverquill-classes/1')
    _class = Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

    assert _class.description == class_description.value
    
    new_class_description = ClassDescription('Learn new technics to induce your listeners.')
    _class.update_description(new_description=new_class_description)
    
    assert _class.description == new_class_description.value

def test_update_class_college_id() -> None:
    class_name=ClassName('Dialogue Technics I')
    class_description=ClassDescription('Learn how to convince your listeners by your best weapon, dialogues.')
    class_college_id=ClassCollegeID(2)
    class_image_url=ClassImageUrl('https://strixhaven.com/silverquill-classes/1')
    _class = Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

    assert _class.college_id == class_college_id.value
    
    new_class_college_id = ClassCollegeID(3)
    _class.update_college_id(new_college_id=new_class_college_id)
    
    assert _class.college_id == new_class_college_id.value

def test_update_class_image_url() -> None:
    class_name=ClassName('Dialogue Technics I')
    class_description=ClassDescription('Learn how to convince your listeners by your best weapon, dialogues.')
    class_college_id=ClassCollegeID(2)
    class_image_url=ClassImageUrl('https://strixhaven.com/silverquill-classes/1')
    _class = Class.create(
        name=class_name,
        description=class_description,
        college_id=class_college_id,
        image_url=class_image_url
    )

    assert _class.image_url == class_image_url.value
    
    new_class_image_url = ClassImageUrl('https://strixhaven.com/silverquill-classes/15')
    _class.update_image_url(new_image_url=new_class_image_url)
    
    assert _class.image_url == new_class_image_url.value
