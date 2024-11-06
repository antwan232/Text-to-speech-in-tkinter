import tkinter as tk # tkinter Liberary
from tkinter import *
from tkinter import ttk # ttk: collection of widgets like buttons etc ...
from PIL import Image ,ImageTk
import windows
import tkinter.font as font
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# root configeration 
root = tk.Tk() # Create TK opject => main window of our application
root.geometry('900x450+200+200') # Set fixed window width:height
root.title("Text to speech")
root.resizable(False, False)
root.configure(bg='#305065')
root.columnconfigure(0, weight=1)

# main font 
# default_font = font.nametofont('TkDefaultFont')
# default_font.configure(size=12)

# logo img
logo_photo = Image.open('img/logo.jpeg').resize((70,70))
logo_img = ImageTk.PhotoImage(logo_photo)
root.iconphoto(True, logo_img)

# Get style database
style = ttk.Style(root)  
# style.theme_use('clam')