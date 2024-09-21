import reflex as rx
from TeleLisa.styles.colors import Colors, TextColors


BASE_STYLES = {
    rx.button: {
        "cursor": "pointer"
    },
    rx.text: {
        "color": TextColors.BODY.value
    },
    rx.button: {
        "backgroundColor" : Colors.BUTTON_BACKGROUND.value,
        "color" : TextColors.BODY.value
    },
    rx.select: {
        "color" : TextColors.BODY.value,
    },
    rx.link: {
        "color" : Colors.PRIMARY.value
    }
    # rx.hstack: {
    #     "width": "100%"
    # },
    # rx.box: {
    #     "width": "100%"
    # },
    # rx.vstack: {
    #     "width": "100%"
    # },
    # rx.flex: {
    #     "width": "100%"
    # }
}