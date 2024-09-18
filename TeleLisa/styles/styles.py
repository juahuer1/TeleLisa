import reflex as rx
from enum import Enum

######## VARS
spacing = 5

class Size(Enum):
    XS = "0.8em"
    S = "1em"
    L = "2em"
    XL= "4em"
    XXL="6em"
    Extra_4="10em"
    Extra_5="15em"


spacing_values = [
    4,   # --space-1
    8,   # --space-2
    12,  # --space-3
    16,  # --space-4
    24,  # --space-5
    32,  # --space-6
    40,  # --space-7
    48,  # --space-8
    64   # --space-9
]

######## STYLES DESKTOP
## MAIN PAGE
body_style = dict(
    max_width="85%",
    align_items="center",
    overflow="auto",
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
        # border_radius="25%",
    )

# FOOTER
class footer():
    footer_container = dict(
        width="100%",
        padding_left = Size.S,
        padding_right = Size.S,
        margin_top=f"{spacing_values[spacing-1]}px"
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
    header_style = dict(
        margin_top=f"{spacing_values[spacing-1]}px", # En reflex depende tambien de data-scaling pero de momento funciona bien así
    )

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
        margin_top=f"{spacing_values[spacing-1]}px",
        width="100%"
    )

    menu_container_style = dict(
        width = "100%",
        display="grid"
    )


######## STYLES MOBILE
## NAVBAR

# navbar_title_style = dict(
#     size="6", 
#     weight="bold"
# )

# navbar_image_style = dict(
#     width="2em",
#     height="auto",
#     border_radius="25%",
# )