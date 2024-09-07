import reflex as rx
import TeleLisa.styles.styles as styles

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(src="/favicon.ico", size="8"),
        rx.vstack(
            rx.heading("Bienvenido a TeleLisa", size="7"),
            rx.text(
                "No has fantaseado con poder ver Los Simpsons 24/7?",
                size="3",
            )
        ),
        margin_top=styles.Size.XL,
        padding = styles.Size.L
    )