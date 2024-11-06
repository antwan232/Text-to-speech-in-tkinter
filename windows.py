# make tkinter look nicly

from ctypes import WinDLL
shcore = WinDLL('shcore')  # access the Windows "shcore" DLL (library)
shcore.SetProcessDpiAwareness(1)