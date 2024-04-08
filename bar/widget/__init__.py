from libqtile import widget
from .config_wigets import config_widgets


widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)

widgets = config_widgets()
extension_defaults = widget_defaults.copy()

widget_principal = [
    *widgets.workspace(),

    # widget.Prompt(),
    # widget.WindowName(),
    
    # widget.Chord(
    #     chords_colors={
    #         "launch": ("#ff0000", "#ffffff"),
    #     },
    #     name_transform=lambda name: name.upper(),
    # ),
    # widget.TextBox("default config", name="default"),
    # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # widget.StatusNotifier(),
    # widget.Systray(),
    *widgets.view_setup(),
    # widget.QuickExit(),
]

widgets_secundary = [
    *widgets.workspace()
]
