import reflex as rx
import TeleLisa.styles.styles as styles

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", "/#"),
        spacing="3",
        justify="end",
        style=styles.footer.socials_def
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.text("Powered by"), 
                        href="https://reflex.dev/",
                    ),
                    rx.image(
                        src="/img/reflex.svg",
                    ),
                    style=styles.footer.powered_by_container
                ),
                socials(),
                justify="between",
                style=styles.footer.socials_container
            ),
            width="100%",
        ),
        style=styles.footer.footer_container
    )