# -*- coding: utf-8
import urwid


class MainWindow(urwid.Frame):

    def __init__(self, l_widget, r_widget):
        panels = urwid.AttrMap(
            urwid.Columns([l_widget, r_widget]), 'panels', None)

        header = urwid.AttrMap(urwid.Text('  F1 Help  '), 'header', None)

        footer = urwid.AttrMap(
            urwid.Text('  Containers: 0  |  Running: 0  '), 'footer', None)

        urwid.Frame.__init__(self, panels, header, footer)


class ContainerList(urwid.ListBox):

    items = None

    def __init__(self, containers):
        self.items = self.create_list_items(containers)
        body = urwid.SimpleListWalker(self.items)
        urwid.ListBox.__init__(self, body)

    def format_item_text(self, container):
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(
            container['Id'],
            container['Image'],
            container['Command'],
            container['Created'],
            container['Status'],
            container['Ports'],
            container['Names']
        )

    def create_list_items(self, containers):
        # items = [urwid.AttrMap(w, None, "selection") for w in [
        #     urwid.Text(self.format_item_text(c)) for c in containers
        # ]]
        items = []
        keys = ['Id', 'Image', 'Command', 'Created', 'Status', 'Ports', 'Names']
        for c in containers:
            item = urwid.AttrWrap(
                urwid.GridFlow(
                    [urwid.Text(c[k]) for k in keys], 20, 3, 0, 'left'),
                None, 'selection')
            items.append(item)
        return items

    def on_keyup(self):
        try:
            cur_wid, cur_pos = self.body.get_focus()
            prv_wid, prv_pos = self.body.get_prev(cur_pos)
            self.body.set_focus(prv_pos)
        except:
            pass

    def on_keydn(self):
        try:
            cur_wid, cur_pos = self.body.get_focus()
            nxt_wid, nxt_pos = self.body.get_next(cur_pos)
            self.body.set_focus(nxt_pos)
        except:
            pass
