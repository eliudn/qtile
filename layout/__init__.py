from libqtile import layout
import sys
sys.path.append('/home/devleunamz/.config/qtile/')
from themes.color import all_color as color


full_layouts = [
    layout.Columns(
        border_focus_stack=color["color1"], 
        border_focus = color["color2"],
        border_width=4, 
        margin=10,
        border_normal = color["backgraund_secundary"],
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
