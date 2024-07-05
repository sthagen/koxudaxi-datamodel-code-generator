# generated by datamodel-codegen:
#   filename:  const.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from msgspec import Meta, Struct
from typing_extensions import Annotated, Literal


class Api(Struct):
    version: Annotated[Literal['v1'], Meta(description='The version of this API')]