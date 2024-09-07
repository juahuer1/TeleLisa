import reflex as rx
import TeleLisa.styles.styles as styles
from rxconfig import config


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=config.favicon,
            size="8",
            style=styles.avatar_style,
            radius="full"
            ),
        rx.vstack(
            rx.heading(
                "Bienvenido a TeleLisa",
                size="7"
                ),
            rx.text(
                "No has fantaseado con poder ver Los Simpsons 24/7?",
                size="3",
            )
        ),
        style=styles.header_style
    )