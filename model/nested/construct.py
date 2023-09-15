from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int
    name: str = 'John'



if __name__ == '__main__':
    original_user = User(id=123, age=23)

    user_data = original_user.model_dump()
    print('model_dump', user_data)
    field_set = original_user.model_fields_set
    print('model_fields_set', field_set)
    new_user = User.model_construct(_fields_set=field_set, **user_data)
    print(repr(new_user))
