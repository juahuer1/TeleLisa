import reflex as rx
import TeleLisa.styles.styles as styles

def RxGrid(data, columns: str = "3", spacing: str = styles.Size.DEFAULT.value, width: str = "100%", **kwargs) -> rx.Component:
    return rx.grid(
        data,
        columns = columns,
        spacing = spacing,
        width=width,
        **kwargs
    )

def RxLink(data, href: str, is_external: bool = True, **kwargs) -> rx.Component:
    return rx.link(
        data,
        href=href,
        is_external=is_external,
        **kwargs
    )

def RxButton(data, color_scheme: str = "brown", size: str = styles.BTN_SIZE, **kwargs) -> rx.Component:
    return rx.button(
        data,
        color_scheme=color_scheme,
        size=size,
        **kwargs
    )

def RxSelect(data, color_scheme: str = "brown", variant: str = "soft", size: str = styles.BTN_SIZE, placeholder: str = "Seleccione...", **kwargs) -> rx.Component:
    return rx.select(
        data,
        color_scheme=color_scheme,
        variant=variant,
        size="3",
        placeholder=placeholder,
        **kwargs
    )

def RxText(data, size: str = styles.TextSizes.DEFAULT.value, **kwargs) -> rx.Component:
    return rx.text(
        data,
        size=size,
        **kwargs
    )