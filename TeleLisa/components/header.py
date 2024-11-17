import reflex as rx
import TeleLisa.styles.styles as styles
from TeleLisa.styles.colors import Colors, TextColors
from rxconfig import config
from TeleLisa.elements.elements import RxText


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src="/img/lisa-feliz.jpg",
                size="8",
                radius="full",
                style=styles.header.avatar_style,
            ),
            rx.vstack(
                rx.heading(
                    "Bienvenido a TeleLisa",
                    size=styles.Size.BIG.value,
                ),
                RxText(
                    "No has fantaseado con poder ver Los Simpsons 24/7?",
                ),
                spacing=styles.Size.EXTRA_SMALL.value
            ),
            spacing=styles.Size.DEFAULT.value,
            align="center"
        )    
    )
    