"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import TeleLisa.styles.styles as styles
from TeleLisa.styles.global_styles import BASE_STYLES
from TeleLisa.components.navbar import navbar
from TeleLisa.components.header import header
from TeleLisa.components.tv import tv
from TeleLisa.components.footer import footer
from TeleLisa.components.season_menu import season_menu
from TeleLisa.components.episode_view import episode_view



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
                style=styles.body_style,
                spacing=styles.Size.DEFAULT.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )

def wiki() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                season_menu(),   
                episode_view(),
                style=styles.body_style,
                spacing=styles.Size.DEFAULT.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )


app = rx.App(
    style=BASE_STYLES
)
app.add_page(index)
app.add_page(wiki)
