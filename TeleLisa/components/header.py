import reflex as rx
import TeleLisa.styles.styles as styles
from rxconfig import config


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src="/img/lisa-feliz.jpg",
            size="8",
            radius="full",
            style=styles.header.avatar_style,
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
    )