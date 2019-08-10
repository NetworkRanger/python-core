#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 9:39 PM

from Tkinter import Tk, Frame, Label, Button, BOTH
import os
import tempfile
import win32.client as win32

def edit():
    olook = win32.Dispatch('Outlook.Appliction')
    insp = olook.ActiveInspector()
    if insp is None:
        return
    item = insp.CurrentItem
    if item is None:
        return

    body = item.body
    tmpfd, tmpfn = tempfile.mkstemp()
    f = os.fdopen(tmpfd, 'a')
    f.write(body.encode('ascii', 'ignore').replace('\r\n'), '\n')
    f.close()

    # ed = r"d:\emacs-23.2\bin\emcasclientw.exe"
    ed = r"c:\progra~1\vim\vim73\gvim.exe"
    os.spawnv(os.P_WAIT, ed, [ed, tmpfn])

    f = open(tmpfn, 'r')
    body = f.read().replace('\n', '\r\n')
    f.close()
    os.unlink(tmpfn)
    item.Body = body


if __name__ == '__main__':
    tk = Tk()
    f = Frame(tk, borderwith=2)
    f.pack(fill=BOTH)
    Label(f, text='Outlook Edit Launcher v0.3').pack()
    Button(f, text='Edit', fg='blue', command=edit).pack(fill=BOTH)
    Button(f, text='Quit', fg='red', command=tk.quit).pack(fill=BOTH)
    tk.mainloop()