from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, ValidationError

DataT = TypeVar('DataT')


class Error(BaseModel):
    code: int
    message: str


class DataModel(BaseModel):
    numbers: List[int]
    people: List[str]


class Response(BaseModel, Generic[DataT]):
    data: Optional[DataT] = None


data = DataModel(numbers=[1, 2, 3], people=[])
print(data)

error = Error(code=404, message='Not Found')
print(Response[int](data=1))
print(Response[str](data='value'))
print(Response[str](data='value').model_dump())
print(Response[DataModel](data=data))

try:
    Response[int](data='value')
except ValidationError as ve:
    print(ve)
