import reflex as rx
import Telelisa.styles.styles_desktop as styles_desktop
import Telelisa.styles.styles_mobile as styles_mobile
import Telelisa.dict.dict as dict 
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src=dict.Site.FAVICON,
                        style=styles_desktop.navbar_image_style
                    ),
                    rx.heading(
                        dict.Site.TITLE,
                        style=styles_desktop.navbar_title_style
                    ),
                    align="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Wiki", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src=dict.Site.FAVICON,
                        style=styles_mobile.navbar_image_style
                    ),
                    rx.heading(
                        dict.Site.TITLE,
                        style=styles_mobile.navbar_title_style
                    ),
                    align="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("Wiki"),
                    ),
                    justify="end",
                ),
                justify="between",
                align="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="999",
        width="100%",
    )