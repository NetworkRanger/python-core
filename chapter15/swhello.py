#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 6:17 PM

from pawt import swing
import sys
from java.awt import Color, BorderLayout

def quit(e):
    sys.exit()

top = swing.JFrame("PySwing")
box = swing.JPanel()
hello = swing.JButton("QUIT", actionPerformed=quit, background=Color.red, foreground=Color.white)

box.add("North", hello)
box.add("Sourth", quit)
top.contentPane.add(box)
top.pack()
top.visible = 1 # or True for Jython 2.2+

