from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    name_id: str = ''.join(['id', 'name'])


def main(id_) -> User:
    return User(id=id_)


if __name__ == '__main__':
    user = main(123)
    assert user.id == 123
    assert user.name == 'John Doe'
    assert user.model_fields_set == {'id'}
    assert user.model_dump() == {
        'id': 123, 'name': 'John Doe', 'name_id': 'idname'
    }
    user.id = 321
    assert user.id == 321
    print('model_dump_json', user.model_dump_json())
    print('model_extra', user.model_extra)
    print('model_field_set', user.model_fields_set)
    print('model_json_schema', user.model_json_schema())
    # print('model_modify_json_schema', user.model_modify_json_schema())
    # print('model_parametrized_name', user.model_parametrized_name())
    # print('model_validate_json', user.model_validate_json())
