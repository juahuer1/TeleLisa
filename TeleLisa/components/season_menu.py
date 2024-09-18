import reflex as rx
import TeleLisa.styles.styles as styles

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

first_block = rx.hstack(
    rx.link(rx.text("Temporada 1"), href="#"),
    rx.link(rx.text("Temporada 2"), href="#"),
    rx.link(rx.text("Temporada 3"), href="#"),
    rx.link(rx.text("Temporada 4"), href="#"),
    rx.link(rx.text("Temporada 5"), href="#"),
    rx.link(rx.text("Temporada 6"), href="#"),
    rx.link(rx.text("Temporada 7"), href="#"),
    rx.link(rx.text("Temporada 8"), href="#"),
    rx.link(rx.text("Temporada 9"), href="#"),
    rx.link(rx.text("Temporada 10"), href="#"),
    display=menuState.first_items_display,
    width="100%"
)

second_block = rx.hstack(
    rx.link(rx.text("Temporada 11"), href="#"),
    rx.link(rx.text("Temporada 12"), href="#"),
    rx.link(rx.text("Temporada 13"), href="#"),
    rx.link(rx.text("Temporada 14"), href="#"),
    rx.link(rx.text("Temporada 15"), href="#"),
    rx.link(rx.text("Temporada 16"), href="#"),
    rx.link(rx.text("Temporada 17"), href="#"),
    rx.link(rx.text("Temporada 18"), href="#"),
    rx.link(rx.text("Temporada 19"), href="#"),
    rx.link(rx.text("Temporada 20"), href="#"),
    display=menuState.last_items_display,
)

def season_menu() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.button(
                rx.icon(
                    "arrow-big-left",
                ),
                disabled=menuState.show_less_button_disabled,
                on_click=menuState.showLess
            ),
            first_block,
            second_block,
            rx.button(
                rx.icon(
                    "arrow-big-right"
                ),
                disabled=menuState.show_more_button_disabled,
                on_click=menuState.showMore
            ),
            
            justify="between",
            align="center",
            style=styles.season_menu.menu_style,
        ),
        style=styles.season_menu.menu_container_style,
    )

