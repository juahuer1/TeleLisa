import reflex as rx
import TeleLisa.styles.styles as styles
from rxconfig import config


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
                        src=config.favicon,
                        style=styles.navbar.navbar_image_style
                    ),
                    rx.heading(
                        config.app_name,
                        style=styles.navbar.navbar_title_style
                    ),
                    align="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Wiki", "/wiki"),
                    navbar_link("About Us", "/#"),
                    justify="end",
                    spacing="5",
                ),
                rx.hstack(
                    rx.color_mode.button(),
                ),
                justify="between",
                align="center",
            ),
        ),
        # rx.mobile_and_tablet(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.image(
        #                 src=dict.Site.FAVICON,
        #                 style=styles_mobile.navbar_image_style
        #             ),
        #             rx.heading(
        #                 dict.Site.TITLE,
        #                 style=styles_mobile.navbar_title_style
        #             ),
        #             align="center",
        #         ),
        #         rx.menu.root(
        #             rx.menu.trigger(
        #                 rx.icon("menu", size=30)
        #             ),
        #             rx.menu.content(
        #                 rx.menu.item("Home"),
        #                 rx.menu.item("Wiki"),
        #             ),
        #             justify="end",
        #         ),
        #         justify="between",
        #         align="center",
        #     ),
        # ),
        style=styles.navbar.navbar_style
    )