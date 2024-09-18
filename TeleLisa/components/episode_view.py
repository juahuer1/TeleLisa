import reflex as rx
import TeleLisa.styles.styles as styles

def episode_view()->rx.Component:
    return rx.box(
        rx.grid(
            rx.foreach(
                rx.Var.range(6),
                lambda i: rx.card(
                    rx.hstack(
                        rx.image(src="/img/lisa-feliz.jpg", width=styles.Size.Extra_5, height="auto"),
                        rx.vstack(
                            rx.heading(f"Chapter {i + 1}"),
                            rx.text("En este capítulo, exploraremos los fundamentos de la programación, incluyendo los conceptos básicos de variables, estructuras de control y tipos de datos. Al finalizar, estarás listo para escribir tus primeros programas en Python.")
                        )
                        
                    )
                ),
            ),
            columns="3",
            spacing=f"{styles.SPACING}",
            width="100%",
        )
    )