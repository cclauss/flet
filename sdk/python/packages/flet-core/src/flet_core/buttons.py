from dataclasses import dataclass, field
from typing import Optional

from flet_core.alignment import Alignment
from flet_core.border import BorderSide
from flet_core.text_style import TextStyle
from flet_core.types import (
    BorderRadiusValue,
    ControlState,
    ControlStateValue,
    MouseCursor,
    OptionalNumber,
    PaddingValue,
    VisualDensity,
)


@dataclass
class OutlinedBorder:
    pass


@dataclass
class StadiumBorder(OutlinedBorder):
    def __post_init__(self):
        self.type = "stadium"


@dataclass
class RoundedRectangleBorder(OutlinedBorder):
    radius: BorderRadiusValue = None

    def __post_init__(self):
        self.type = "roundedRectangle"


@dataclass
class CircleBorder(OutlinedBorder):
    type: str = field(default="circle")


@dataclass
class BeveledRectangleBorder(OutlinedBorder):
    radius: BorderRadiusValue = None

    def __post_init__(self):
        self.type = "beveledRectangle"


@dataclass
class ContinuousRectangleBorder(OutlinedBorder):
    radius: BorderRadiusValue = None

    def __post_init__(self):
        self.type = "continuousRectangle"


@dataclass
class ButtonStyle:
    color: ControlStateValue[str] = None
    bgcolor: ControlStateValue[str] = None
    overlay_color: ControlStateValue[str] = None
    shadow_color: ControlStateValue[str] = None
    surface_tint_color: ControlStateValue[str] = None
    elevation: ControlStateValue[OptionalNumber] = None
    animation_duration: Optional[int] = None
    padding: ControlStateValue[PaddingValue] = None
    side: ControlStateValue[BorderSide] = None
    shape: ControlStateValue[OutlinedBorder] = None
    alignment: Optional[Alignment] = None
    enable_feedback: Optional[bool] = None
    text_style: ControlStateValue[TextStyle] = None
    icon_size: ControlStateValue[OptionalNumber] = None
    icon_color: ControlStateValue[str] = None
    visual_density: Optional[VisualDensity] = None
    mouse_cursor: ControlStateValue[MouseCursor] = None

    def __post_init__(self):
        if not isinstance(self.text_style, dict):
            self.text_style = {ControlState.DEFAULT: self.text_style}

        if not isinstance(self.padding, dict):
            self.padding = {ControlState.DEFAULT: self.padding}

        if not isinstance(self.side, dict):
            self.side = {ControlState.DEFAULT: self.side}

        if not isinstance(self.shape, dict):
            self.shape = {ControlState.DEFAULT: self.shape}
