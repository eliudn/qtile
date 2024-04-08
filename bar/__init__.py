from libqtile import widget, bar
from libqtile.config import Screen
from .status_bar import general_bar
from .widget import widget_principal, widgets_secundary



bar_principal = [
    Screen(
        
        top= general_bar(
            widget_principal

        )
    ),
    Screen(
        top=general_bar(
                widgets_secundary
        )
    )
]

