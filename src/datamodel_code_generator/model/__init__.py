from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Callable, Iterable, List, NamedTuple, Optional, Type

from .. import DatetimeClassType, PythonVersion
from ..types import DataTypeManager as DataTypeManagerABC
from .base import ConstraintsBase, DataModel, DataModelFieldBase

if TYPE_CHECKING:
    from .. import DataModelType

DEFAULT_TARGET_DATETIME_CLASS = DatetimeClassType.Datetime
DEFAULT_TARGET_PYTHON_VERSION = PythonVersion(f'{sys.version_info.major}.{sys.version_info.minor}')


class DataModelSet(NamedTuple):
    data_model: Type[DataModel]
    root_model: Type[DataModel]
    field_model: Type[DataModelFieldBase]
    data_type_manager: Type[DataTypeManagerABC]
    dump_resolve_reference_action: Optional[Callable[[Iterable[str]], str]]
    known_third_party: Optional[List[str]] = None


def get_data_model_types(
    data_model_type: DataModelType,
    target_python_version: PythonVersion = DEFAULT_TARGET_PYTHON_VERSION,
    target_datetime_class: Optional[DatetimeClassType] = None,
) -> DataModelSet:
    from .. import DataModelType
    from . import dataclass, msgspec, pydantic, pydantic_v2, rootmodel, typed_dict
    from .types import DataTypeManager

    if target_datetime_class is None:
        target_datetime_class = DEFAULT_TARGET_DATETIME_CLASS
    if data_model_type == DataModelType.PydanticBaseModel:
        return DataModelSet(
            data_model=pydantic.BaseModel,
            root_model=pydantic.CustomRootType,
            field_model=pydantic.DataModelField,
            data_type_manager=pydantic.DataTypeManager,
            dump_resolve_reference_action=pydantic.dump_resolve_reference_action,
        )
    elif data_model_type == DataModelType.PydanticV2BaseModel:
        return DataModelSet(
            data_model=pydantic_v2.BaseModel,
            root_model=pydantic_v2.RootModel,
            field_model=pydantic_v2.DataModelField,
            data_type_manager=pydantic_v2.DataTypeManager,
            dump_resolve_reference_action=pydantic_v2.dump_resolve_reference_action,
        )
    elif data_model_type == DataModelType.DataclassesDataclass:
        return DataModelSet(
            data_model=dataclass.DataClass,
            root_model=rootmodel.RootModel,
            field_model=dataclass.DataModelField,
            data_type_manager=dataclass.DataTypeManager,
            dump_resolve_reference_action=None,
        )
    elif data_model_type == DataModelType.TypingTypedDict:
        return DataModelSet(
            data_model=(typed_dict.TypedDict if target_python_version.has_typed_dict else typed_dict.TypedDictBackport),
            root_model=rootmodel.RootModel,
            field_model=(
                typed_dict.DataModelField
                if target_python_version.has_typed_dict_non_required
                else typed_dict.DataModelFieldBackport
            ),
            data_type_manager=DataTypeManager,
            dump_resolve_reference_action=None,
        )
    elif data_model_type == DataModelType.MsgspecStruct:
        return DataModelSet(
            data_model=msgspec.Struct,
            root_model=msgspec.RootModel,
            field_model=msgspec.DataModelField,
            data_type_manager=msgspec.DataTypeManager,
            dump_resolve_reference_action=None,
            known_third_party=['msgspec'],
        )
    raise ValueError(f'{data_model_type} is unsupported data model type')  # pragma: no cover


__all__ = ['ConstraintsBase', 'DataModel', 'DataModelFieldBase']
