import reflex as rx
import TeleLisa.styles.styles as styles
from TeleLisa.elements.elements import RxButton

class menuState(rx.State):
    first_items_display: str = "flex"
    last_items_display: str = "none"
    show_more_button_disabled: bool = False
    show_less_button_disabled: bool = True

    def showMore(self):
        self.first_items_display = "none"
        self.last_items_display = "flex"
        self.show_more_button_disabled = True
        self.show_less_button_disabled = False

    def showLess(self):
        self.last_items_display = "none"
        self.first_items_display = "flex"
        self.show_more_button_disabled = False
        self.show_less_button_disabled = True

temporadas = [f"Temporada {i}" for i in range(1, 11)]

first_block = rx.hstack(
    rx.foreach(
        temporadas,
        lambda temporada: 
            RxButton(
                temporada,
                variant="ghost",
            ),

    ),
    display=menuState.first_items_display,
    justify="center",
    spacing=styles.Size.DEFAULT.value
)

temporadas = [f"Temporada {i}" for i in range(11, 21)]

second_block = rx.hstack(
    rx.foreach(
        temporadas,
        lambda temporada:
            RxButton(
                temporada,
                variant="ghost",
            ),
    ),
    display=menuState.last_items_display,
    justify="center",
    spacing=styles.Size.DEFAULT.value
)

def season_menu() -> rx.Component:
    return rx.box(
        rx.hstack(
            RxButton(
                rx.icon(
                    "arrow-big-left",
                ),
                disabled=menuState.show_less_button_disabled,
                on_click=menuState.showLess,
            ),
            first_block,
            second_block,
            RxButton(
                rx.icon(
                    "arrow-big-right"
                ),
                disabled=menuState.show_more_button_disabled,
                on_click=menuState.showMore,
            ),
            justify="between",
            align="center",
            style=styles.season_menu.menu_style,
        ),
        style=styles.season_menu.menu_container_style,
    )

