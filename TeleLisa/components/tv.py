import reflex as rx
import TeleLisa.styles.styles as styles
from rxconfig import config


def tv() -> rx.Component:
    return rx.hstack(
        rx.video(
            url="/video/test.mp4",
            style=styles.tv.tv_video_style
        ),
        rx.vstack(
            rx.text("Puedes seleccionar otro capítulo para reproducir:"),
            rx.hstack(
                 rx.select(["Temporada 1", "Temporada 2", "Temporada 3", "Temporada 4", "Temporada 5"],
                    default_value="Temporada 1"      
                ),
                rx.select(["Episodio 1", "Episodio 2", "Episodio 3", "Episodio 4", "Episodio 5"],
                    default_value="Episodio 1"
                ),
                rx.button("Reproducir", color_scheme="blue")
            ),
            rx.text("Descripcion del capítulo..."),
            style=styles.tv.vstack_style
        ),        
    ),
