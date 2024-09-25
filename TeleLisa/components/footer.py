import reflex as rx
import TeleLisa.styles.styles as styles
from TeleLisa.styles.colors import Colors
from rxconfig import config
from TeleLisa.elements.elements import RxLink, RxText

def social_link(icon: str, href: str) -> rx.Component:
    return RxLink(
        rx.icon(
            icon,
            style=styles.footer.social_icon_styles
        ),
        href=href,
        
    )


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", config.github),
        spacing=styles.Size.SMALL.value,
        justify="end",
        style=styles.footer.socials_def
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    RxLink(
                        rx.hstack(
                            RxText(
                                "Powered by",
                                color = Colors.PRIMARY.value,
                            ), 
                            rx.image(   
                                src="/img/reflex.svg",
                            ),
                            align="center"
                        ),    
                        href="https://reflex.dev/",  
                    ),
                    style=styles.footer.powered_by_container
                ),
                socials(),
                justify="between",
                style=styles.footer.socials_container
            ),
            style=styles.footer.vstack_container
        ),
        style=styles.footer.footer_container
    )