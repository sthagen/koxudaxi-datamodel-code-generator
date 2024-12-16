# generated by datamodel-codegen:
#   filename:  inner_folder/schema.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import ClassVar, Literal, Union

from msgspec import Meta, Struct
from typing_extensions import Annotated

from .. import type_4
from ..subfolder import type_5
from . import type_2
from .artificial_folder import type_1


class Type3(Struct, tag_field='type_', tag='c'):
    type_: ClassVar[Annotated[Literal['c'], Meta(title='Type ')]] = 'c'


class Response(Struct):
    inner: Annotated[
        Union[type_1.Type1, type_2.Type2, Type3, type_4.Type4, type_5.Type5],
        Meta(title='Inner'),
    ]