"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import TeleLisa.styles.styles as styles
from TeleLisa.components.navbar import navbar
from TeleLisa.components.header import header
from TeleLisa.components.tv import tv

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                tv(),
                style=styles.main_page_style,
                spacing=f"{styles.spacing}"
            ),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
