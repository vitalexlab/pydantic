from pydantic import BaseModel, conint
from typing_extensions import Union


class SuccessResult(BaseModel):
    score: conint(ge=0, le=100)


class ErrorResult(BaseModel):
    first: list
    second: list
    common: list


class Response(BaseModel):
    status: str
    result: Union[SuccessResult, ErrorResult]


if __name__ == "__main__":
    json_ex = """{"status": "ok", "result": {"score": 1011}}"""
    resp = Response.model_validate_json(json_ex)
    print(resp)

