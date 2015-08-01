# -*- coding: utf-8
import urwid


class FocusListBox(urwid.ListBox):
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
