import reflex as rx
from enum import Enum

######## CONSTANTS
SPACING = 5

class Size(Enum):
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
    overflow="auto",
    margin_y=f"{spacing_values[SPACING-1]}px"
)

main_page_style = dict(
    padding_top="68px",
)

# NAVBAR
class navbar():
    navbar_style = dict(
        bg=rx.color("accent", 3),
        padding=Size.S,
        position="fixed",
        top="0px",
        z_index="999",
        width="100%",
        heigth=Size.XL
    )

    navbar_title_style = dict(
        size="7", 
        weight="bold"
    )

    navbar_image_style = dict(
        width="2.25em",
        height="auto",
    )

# FOOTER
class footer():
    footer_container = dict(
        width="100%",
        padding_left = Size.S,
        padding_right = Size.S,
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

# HEADER
class header():
    avatar_style = dict(
        margin_left = Size.S,
    )

# TV
class tv():
    tv_video_style = dict(
        flex_shrink = "0",  # No se encogerá
        flex_grow = "0",    # No crecerá
    )

    vstack_style = dict(
        margin_left = Size.S,
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


######## STYLES MOBILE