from libqtile import bar
import sys
sys.path.append('/home/devleunamz/.config/qtile/')
from themes.color import all_color


def general_bar(widgets):
    return  bar.Bar(
        widgets,
        31,
        background =all_color["transparent"],
        border_color =all_color["transparent"],
        border_width = 0,
        margin = 4,
        opacity = 1
    )
