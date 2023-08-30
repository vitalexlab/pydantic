from typing import List, Optional

from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: Optional[float] = None


class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


def main() -> Spam:
    m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    return m


if __name__ == '__main__':
    n = main()
    print(type(n), n)
    print('model_dump_json', type(n.model_dump_json()), n.model_dump_json())
