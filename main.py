# -*- coding: utf-8
import urwid
from widgets import MainWindow, ContainerList

"""
Safe colors:

'black', 'dark red', 'dark green', 'brown', 'dark blue',
'dark magenta', 'dark cyan', 'light gray', 'dark gray',
'light red', 'light green', 'yellow', 'light blue',
'light magenta', 'light cyan', 'white'
"""


class SimpleCli():

    top = None
    listbox = None
    info = None
    info_container = None

    palette = [
        ("top", "white", "black"),
        ("selection", "black", "dark gray", "standout"),
        ("panels", "white", "dark blue"),
        ('header', 'light gray', 'black', 'bold'),
        ('footer', 'light gray', 'black', 'bold'),
    ]

    containers = [{
        'Id': '12345',
        'Image': 'ubuntu:latest',
        'Command': '/usr/bin/bash',
        'Created': '2 days ago',
        'Status': 'Running',
        'Ports': '8080:80',
        'Names': 'kate-blanchett'
    }, {
        'Id': '78901',
        'Image': 'busybox:latest',
        'Command': 'run.sh',
        'Created': '3 hours ago',
        'Status': 'Stopped',
        'Ports': '',
        'Names': 'tom-cruise'
    }, {
        'Id': '23456',
        'Image': 'mysql:5.6',
        'Command': 'mysqld start',
        'Created': '1 hour ago',
        'Status': 'Running',
        'Ports': '3306',
        'Names': 'mel-gibson'
    },
    ]

    def handle_input(self, input):
        if input == "enter":
            self.info.original_widget.set_text("key pressed: %s" % input)
        elif input == "up":
            self.listbox.on_keyup()
        elif input == "down":
            self.listbox.on_keydn()
        else:
            raise urwid.ExitMainLoop()

    def run(self):

        self.listbox = ContainerList(self.containers)

        self.info = urwid.LineBox(urwid.Text('<BOO>'))
        self.info_container = urwid.Filler(self.info)

        self.top = MainWindow(self.listbox, self.info_container)

        loop = urwid.MainLoop(
            self.top, self.palette, unhandled_input=self.handle_input)

        loop.screen.set_terminal_properties(colors=256)
        loop.run()


if __name__ == "__main__":
    cli = SimpleCli()
    cli.run()
