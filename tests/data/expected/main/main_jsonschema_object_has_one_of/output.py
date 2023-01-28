# generated by datamodel-codegen:
#   filename:  object_has_one_of.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Union

from pydantic import BaseModel, Extra, Field


class Field2(Enum):
    response_a = 'response_a'


class V2TestItem(BaseModel):
    class Config:
        extra = Extra.allow

    field_2: Field2


class Field1(Enum):
    response_1 = 'response_1'


class V2Test1(V2TestItem):
    class Config:
        extra = Extra.allow

    field_1: Field1


class Field21(Enum):
    response_b = 'response_b'


class V2TestItem1(BaseModel):
    class Config:
        extra = Extra.allow

    field_2: Field21


class Field22(Enum):
    response_c = 'response_c'


class V2TestItem2(BaseModel):
    class Config:
        extra = Extra.allow

    field_2: Field22


class Field11(Enum):
    response_2 = 'response_2'


class V2Test2(V2TestItem1):
    class Config:
        extra = Extra.allow

    field_1: Field11


class V2Test3(V2TestItem2):
    class Config:
        extra = Extra.allow

    field_1: Field11


class V2Test(BaseModel):
    class Config:
        extra = Extra.allow

    __root__: Union[V2Test1, Union[V2Test2, V2Test3]] = Field(..., title='v2_test')
