from typing import Optional, Any

from flet_core.control import Control, auto_properties
from flet_core.ref import Ref
from flet_core.types import OptionalNumber


@auto_properties(
    {
        "height": (OptionalNumber, OptionalNumber, "float", None),
        "thickness": (OptionalNumber, OptionalNumber, "float", None),
        "color": (Optional[str], Optional[str], "str", None),
        "leadingIndent": (OptionalNumber, OptionalNumber, "float", None),
        "trailingIndent": (OptionalNumber, OptionalNumber, "float", None),
    }
)
class Divider(Control):
    """
    A thin horizontal line, with padding on either side.

    In the material design language, this represents a divider.

    Example:
    ```
    import flet as ft


    def main(page: ft.Page):

        page.add(
            ft.Column(
                [
                    ft.Container(
                        bgcolor=ft.colors.AMBER,
                        alignment=ft.alignment.center,
                        expand=True,
                    ),
                    ft.Divider(),
                    ft.Container(
                        bgcolor=ft.colors.PINK, alignment=ft.alignment.center, expand=True
                    ),
                ],
                spacing=0,
                expand=True,
            ),
        )


    ft.app(target=main)

    ```

    -----

    Online docs: https://flet.dev/docs/controls/divider
    """

    def __init__(
        self,
        height: OptionalNumber = None,
        thickness: OptionalNumber = None,
        color: Optional[str] = None,
        leading_indent: OptionalNumber = None,
        trailing_indent: OptionalNumber = None,
        #
        # Control
        #
        ref: Optional[Ref] = None,
        opacity: OptionalNumber = None,
        visible: Optional[bool] = None,
        data: Any = None,
    ):

        Control.__init__(
            self,
            ref=ref,
            opacity=opacity,
            visible=visible,
            data=data,
        )

        self.height = height
        self.thickness = thickness
        self.color = color
        self.leading_indent = leading_indent
        self.trailing_indent = trailing_indent

    def _get_control_name(self):
        return "divider"
