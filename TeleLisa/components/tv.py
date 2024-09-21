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
            rx.text(
                "Puedes seleccionar otro capítulo para reproducir:",
                size=styles.TextSize.M.value
            ),
            rx.hstack(
                 rx.select(["Temporada 1", "Temporada 2", "Temporada 3", "Temporada 4", "Temporada 5"],
                    default_value="Temporada 1",
                    variant="soft",
                    color_scheme="brown" 
                ),
                rx.select(["Episodio 1", "Episodio 2", "Episodio 3", "Episodio 4", "Episodio 5"],
                    default_value="Episodio 1",
                    variant="soft",
                    color_scheme="brown"
                ),
                rx.button("Reproducir"),
                align="center"
            ),
            rx.text("Descripcion del capítulo..."),
            style=styles.tv.vstack_style
        ),  
        style=styles.tv.hstack_container_style
    ),
