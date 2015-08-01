# -*- coding: utf-8
import urwid
from widgets import FocusListBox

"""
Safe colors:

'black', 'dark red', 'dark green', 'brown', 'dark blue',
'dark magenta', 'dark cyan', 'light gray', 'dark gray',
'light red', 'light green', 'yellow', 'light blue',
'light magenta', 'light cyan', 'white'
"""


class SimpleCli():

    top = None
    header = None
    listbox = None

    palette = [
        ("top", "white", "black"),
        ("line", "light green", "dark green", "standout"),
        ("frame", "dark magenta", "white"),
    ]

    def handle_input(self, input):
        if input == "enter":
            self.header.original_widget.set_text("key pressed: %s" % input)
        elif input == "up":
            self.listbox.on_keyup()
        elif input == "down":
            self.listbox.on_keydn()
        else:
            raise urwid.ExitMainLoop()

    def create_list_items(self):
        items = [urwid.AttrMap(widget, None, "line") for widget in [
            urwid.Text("XXXYYYZZZ 05/01/2015 boo-hoo   Stopped"),
            urwid.Text("222333444 06/21/2015 mom-dad   Running"),
            urwid.Text("555YYY777 07/05/2015 some-name Stopped"),
            urwid.Text("XXXAAA888 08/08/2015 tada-nix  Stopped"),
        ]]
        return items

    def run(self):

        self.header = urwid.AttrMap(
            urwid.Text("key pressed :", wrap="clip"), "top")
        self.listbox = FocusListBox(urwid.SimpleListWalker(self.create_list_items()))
        self.top = urwid.AttrMap(
            urwid.Frame(self.listbox, self.header), "frame")

        loop = urwid.MainLoop(
            self.top, self.palette, unhandled_input=self.handle_input)
        loop.screen.set_terminal_properties(colors=256)
        loop.run()


if __name__ == "__main__":
    cli = SimpleCli()
    cli.run()
