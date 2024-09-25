import reflex as rx
from TeleLisa.styles.colors import Colors, TextColors
import TeleLisa.styles.fonts as fonts


BASE_STYLES = {
    "font_family": fonts.Type.DEFAULT,
    "font_weight": fonts.Weight.LIGHT,
    rx.button: {
        "color": TextColors.BODY.value,
        "cursor": "pointer"
    },
    rx.text: {
        "color": TextColors.BODY.value,
    },
    rx.select: {
        "color" : TextColors.BODY.value,
    },
    rx.link: {
        "color" : Colors.PRIMARY.value,
        "text_decoration" : "none",
        "_hover" : {}
    },
    rx.heading: {
        "color" : TextColors.HEADER.value,
        "font_family": fonts.Type.DEFAULT,
        "font_weight": fonts.Weight.MEDIUM
    },
    rx.grid: {
        "width" : "100%"
    }
}