import reflex as rx
from enum import Enum
from .colors import Colors, TextColors
######## CONSTANTS
BTN_SIZE = "3"

class TextSizes(Enum):
    SMALL="1"
    DEFAULT="3"
    BIG="5"
    EXTRA_BIG="7"

class Size(Enum):
    NONE = "0"
    EXTRA_SMALL = "1"
    SMALL = "3"
    DEFAULT = "5"
    BIG = "7"

class EMSize(Enum):
    XS = "0.8em"
    S = "1em"
    L = "2em"
    XL= "4em"
    XXL="6em"
    Extra_4="10em"
    Extra_5="15em"

spacing_values = [4,8,12,16,24,32,40,48,64]

######## STYLES DESKTOP
## MAIN PAGE
body_style = dict(
    max_width="85%",
    align_items="center",
    margin_y=str(spacing_values[int(Size.DEFAULT.value)])+"px",
)

main_page_style = dict(
    padding_top="68px",
    backgroundColor = Colors.BACKGROUND.value,
    minHeight = "100vh",          # Asegura que el fondo cubra toda la pantalla
)

# NAVBAR
class navbar():
    navbar_style = dict(
        bg=Colors.SECONDARY.value,
        padding=EMSize.S,
        position="fixed",
        top="0px",
        z_index="999",
        width="100%",
        heigth=EMSize.XL
    )

    navbar_button = dict(
        color = Colors.PRIMARY.value,
        # boxShadow = "none"
    )

    navbar_title_style = dict(
        size="7", 
        weight="bold",
        color=Colors.PRIMARY.value
    )

    navbar_image_style = dict(
        width=EMSize.L,
        height="auto",
    )

    vstack_links_style = dict(
        width="100%",
    )

# FOOTER
class footer():
    vstack_container = dict(
        width="100%",
    )

    footer_container = dict(
        width="100%",
        padding_left = EMSize.S,
        padding_right = EMSize.S,
    )

    powered_by_container = dict(
        display="flex",
        align_items="center",
        width="100%"
    )

    socials_container = dict(
        width="100%",
    )

    socials_def = dict(
        width="100%",
    )

    social_icon_styles = dict(
        _hover = {
            "color" : Colors.PRIMARY.value
        }
    )

# HEADER
class header():
    avatar_style = dict(
        margin_left = EMSize.S,
    )

# TV
class tv():
    tv_video_style = dict(
        flex_shrink = "0",  # No se encogerá
        flex_grow = "0",    # No crecerá
    )

    vstack_style = dict(
        margin_left = EMSize.S,
    )

    hstack_container_style = dict(
        heigth = "100%"
    ) 

# SEASON MENU
class season_menu():
    menu_style = dict(
        white_space="nowrap",
        width="100%"
    )

    menu_container_style = dict(
        width = "100%",
    )

# EPISODE VIEW
class episode_view():
    header_image_style = dict(
        width=EMSize.Extra_5, 
        height="auto"
    )


######## STYLES MOBILE