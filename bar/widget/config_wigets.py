from libqtile import widget
import sys
sys.path.append('/home/devleunamz/.config/qtile/')

from themes.color import all_color as color

class config_widgets:
    def __init__(self) -> None:
        pass

    def __base(self):
        return {
            "background" : color["backgraund"],
            "foreground" : color["backgraund_secundary"],
        }
    def __clock(self):
        return widget.Clock(
         
            background= color["backgraund"],
            foreground= color["inactive"],
            format = "%a %d | %I:%M:%S %p",
            # fontsize = 13,

            padding = 5,
        ) 
    def __systray(self):
        return widget.Systray(
            **self.__base(),
            padding = 5,
        )
    
    def __icon(self):
        return widget.TextBox(
            background = color["backgraund"],
            text = " ",
            fontsize = 20,
            padding_x =30,
            margin_x = 30,
        )
    def __left(self):
        pass

    def __right(self):
        return widget.TextBox(
            **self.__base(),
            text = "",

        )

    def __seperator_transparent(self):
        return widget.Sep(
            padding = 1,
            linewidth = 10, 
            size_percent = 100,
            foreground = color["transparent"]
        )

    def __seperator(self):
        return widget.Sep(
            **self.__base(),
            padding = 1,
            linewidth = 10, 
            size_percent = 0,

        )

    def __taskList(self):
        return widget.TaskList(
            padding = 5,
            rounded = False,
            border = color["color2"],
            highlight_method = "block",
            max_title_width = 200,
        )


    def __tap(self):
        return widget.GroupBox(
            highlight_method='block',
            background = color["backgraund"],
            foreground = color["backgraund_secundary"],
            block_highlight_text_color= color["backgraund"],
            active = color["active"],
            inactive= color["inactive"],
            # font = "",
            fontsize = 15, 
            highlight_color = color["primary"],
            other_current_screen_border=color["color2"],
            other_screen_border = color["color2"],
            this_current_screen_border = color["primary"],
            this_screen_border = color["secundary"],
            borderwidth= 0,
            margin_x = 4,
            margin_y= 2,
            padding_x = 6,
            padding_y = 3,
            rounded = False,
        )
    def __statusnotifier(self):
        return widget.StatusNotifier(

        )

    def workspace(self) -> list:
        return [

            self.__seperator_transparent(),
            self.__icon(),
            self.__seperator_transparent(),
            self.__tap(),
            self.__seperator_transparent(),
            self.__taskList(),
        ]

    def view_setup(self) -> list:
        return [
            self.__seperator(),
            self.__systray(),
            self.__statusnotifier(),
            self.__seperator(),
            self.__clock(),
            self.__seperator(),
            self.__seperator_transparent(),
        ]
    # widget.Prompt(), ff
    # widget.WindowName(),
    # widget.Chord(
    #     chords_colors={
    #         "launch": ("#ff0000", "#ffffff"),
    #     },
    #     name_transform=lambda name: name.upper(),
    # ),
    # # widget.TextBox("default config", name="default"),
    # # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
    # # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # # widget.StatusNotifier(),
    # widget.Systray(),
    # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    # # widget.QuickExit(),
    #Check_update
