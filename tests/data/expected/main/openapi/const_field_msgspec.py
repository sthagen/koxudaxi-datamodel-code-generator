# generated by datamodel-codegen:
#   filename:  const.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Annotated, Literal

from msgspec import Meta, Struct


class Api(Struct):
    version: Annotated[Literal['v1'], Meta(description='The version of this API')]
