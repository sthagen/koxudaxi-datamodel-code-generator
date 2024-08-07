# generated by datamodel-codegen:
#   filename:  discriminator.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


class Type(Enum):
    my_first_object = 'my_first_object'
    my_second_object = 'my_second_object'
    my_third_object = 'my_third_object'


class ObjectBase(BaseModel):
    name: Optional[str] = Field(None, description='Name of the object')
    type: Literal['type1'] = Field(..., description='Object type')


class CreateObjectRequest(ObjectBase):
    name: str = Field(..., description='Name of the object')
    type: Literal['type2'] = Field(..., description='Object type')


class UpdateObjectRequest(ObjectBase):
    type: Literal['type3']


class Demo(BaseModel):
    __root__: Union[ObjectBase, CreateObjectRequest, UpdateObjectRequest] = Field(
        ..., discriminator='type'
    )
