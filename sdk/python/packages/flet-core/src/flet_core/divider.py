from typing import Any, Optional
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from dataclasses import dataclass


class Attribute:
    def __init__(
        self,
        data_type=None,
        validate=None,
        def_value=None,
        readonly=False,
    ):
        self.data_type = data_type
        self.validate = validate
        self.def_value = def_value
        self.name = None  # This will be set by __set_name__
        self.readonly = readonly

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None) -> object:
        if obj is None:
            return self
        return obj._get_attr(
            self.name, data_type=self.data_type, def_value=self.def_value
        )

    def __set__(self, obj, value) -> None:
        if self.readonly:
            raise AttributeError(f"{self.name} is readonly")
        if not isinstance(value, Attribute):
            if self.validate:
                self.validate(value)
            obj._set_attr(self.name, value)

    @staticmethod
    def positive(value):
        assert value is None or value >= 0, "value cannot be negative"


@dataclass
class Divider(Control):
    height: OptionalNumber = Attribute(data_type="float")
    thickness: OptionalNumber = Attribute(data_type="float")
    color: Optional[str] = Attribute(data_type="string")
    leading_indent: OptionalNumber = Attribute(data_type="float")
    trailing_indent: OptionalNumber = Attribute(data_type="float")
    ref: Optional[Ref] = None
    opacity: OptionalNumber = None
    visible: Optional[bool] = None
    data: Any = None

    def __post_init__(self):
        super().__init__(
            ref=self.ref, opacity=self.opacity, visible=self.visible, data=self.data
        )
        print("Post init")

    def _get_control_name(self):
        return "divider"
