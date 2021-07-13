# Copyright (c) 2021 TomatoSoup
# This file and fastmove are released under GPL

from pyvda import AppView, VirtualDesktop, get_virtual_desktops
import sys

desktopCount = len(get_virtual_desktops())
destDesktop = VirtualDesktop.current().number
temp = destDesktop - 1 # because windows desktops are 1-indexed
direction = sys.argv[1]
if direction == "left":
    destDesktop = ((temp-1)%desktopCount) + 1
elif direction == "right":
    destDesktop = ((temp+1)%desktopCount) + 1
elif direction == "direct":
    destDesktop = int(sys.argv[2])
else:
    print("stop that")
newDesktop = VirtualDesktop(destDesktop)
AppView.current().move(newDesktop)
if (sys.argv[-1] == "follow"):
    newDesktop.go()
