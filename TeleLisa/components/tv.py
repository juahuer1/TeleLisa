import reflex as rx
import TeleLisa.styles.styles as styles
from rxconfig import config
from TeleLisa.elements.elements import RxButton, RxSelect, RxText

def tv() -> rx.Component:
    return rx.hstack(
        rx.video(
            url="/video/test.mp4",
            style=styles.tv.tv_video_style
        ),
        rx.vstack(
            RxText(
                "Puedes seleccionar otro capítulo para reproducir:",
            ),
            rx.hstack(
                RxSelect(["Temporada 1", "Temporada 2", "Temporada 3", "Temporada 4", "Temporada 5"],
                    placeholder="Temporada"
                ),
                RxSelect(["Episodio 1", "Episodio 2", "Episodio 3", "Episodio 4", "Episodio 5"],
                    placeholder="Capitulo"
                ),
                RxButton(
                    "Reproducir",
                ),
                align="center"
            ),
            RxText("Descripcion del capítulo..."),
            spacing=styles.Size.SMALL.value,
            style=styles.tv.vstack_style
        ),  
        style=styles.tv.hstack_container_style
    ),
