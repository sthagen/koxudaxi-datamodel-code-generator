# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List

from typing_extensions import NotRequired, TypedDict


class Pet(TypedDict):
    id: int
    name: str
    tag: NotRequired[str]


Pets = List[Pet]


class User(TypedDict):
    id: int
    name: str
    tag: NotRequired[str]


Users = List[User]


Id = str


Rules = List[str]


class Error(TypedDict):
    code: int
    message: str


class Api(TypedDict):
    apiKey: NotRequired[str]
    apiVersionNumber: NotRequired[str]
    apiUrl: NotRequired[str]
    apiDocumentationUrl: NotRequired[str]


Apis = List[Api]


class Event(TypedDict):
    name: NotRequired[str]


class Result(TypedDict):
    event: NotRequired[Event]
