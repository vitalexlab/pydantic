from pprint import pprint
from typing import List

from pydantic import BaseModel, ValidationError, Field, field_validator


class Tag(BaseModel):
    id: int
    name: str


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')
    # population: int
    # tags: List[Tag]

    @field_validator('name')
    def name_should_be_minsk(cls, v: str) -> str:
        if 'minsk' in v:
            return v
        else:
            raise ValidationError('NOT MINSK!')


def digitaliziruj(json_as_str: str) -> None:
    try:
        city = City.parse_raw(json_as_str)
    except ValidationError as ve:
        pprint(ve.json())
    else:
        pprint(city.model_dump_json(
            by_alias=True,
            exclude={'city_id'}
        ))


if __name__ == '__main__':
    input_json = """
    {
        "city_id": 1,
        "cityFullName": "Minsk",
        "population": 123,
        "tags": [{
            "id": 1, "name": "lol"
        }, {
            "id": 1, "name": "lol"
        }]
    }
    """
    digitaliziruj(input_json)

