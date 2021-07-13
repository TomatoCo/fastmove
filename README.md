# fastmove

Windows 10 has multiple desktops. WinKey + Tab to access them. Cool.  
Windows 10 has a hotkey to switch between these. WinKey+Ctrl+Left/Right. Cooler.  
Windows 10 does not have a hotkey to move your active window between these.

So.

This allows you to do so. There are two parts:  
* The AHK script that watches for key presses and invokes...
* The python script that detects your active window and desktop and moves them.

## Configuration

fastmove requires pyvda and AutoHotKey. `pip install -r requirements.txt` for the first and google for the second.  
Edit onstartup.ahk to include the correct path to the script.  
Tweak the onstartup.ahk script to your liking. The default provides Shift+Ctrl+WinKey+Left/Right to cycle and Shift+Ctrl+WinKey+1-5 to go directly to a window.  
Add `follow` as an additional arg to follow the active window to the new desktop. This can be especially handy because Ctrl+WinKey+Left/Right does not loop around but Shift+Ctrl+WinKey+Left/Right does.  
Consult AHK documentation (again, google) for more details about configuring AHK hotkeys.

## Misc

This was tested on python 3.7.7.  
This uses pyvda as a dependency. This is where the vast majority of the functionality comes from. Find it at https://github.com/mrob95/pyvda  
This uses AutoHotKey to provide performant and global hotkeys. Find it at https://www.autohotkey.com/  
Shift was chosen as the 'extra' modifier because on my Ubuntu laptop it's Ctrl+Alt+Arrows to move desktops and Shift+Ctrl+Alt+Arrows to move active window and desktop. I wanted something analagous to that.  
fastmove is, to be honest, just a few bits of shim code that glue pyvda and some key combos together.  
fastmove is Copyright (c) 2021 TomatoSoup and licensed under the GPL. 