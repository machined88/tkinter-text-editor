import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import os
import functions

class TextEditor:
    def __init__(self, master):
        self.file_select = None

        self.master = master
        self.master.title('Text Editor')
        self.master.geometry("1200x800")
        self.master.iconbitmap("img/notepad.ico")

        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)

        self.menubar = tk.Menu(self.master)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new)
        self.filemenu.add_command(label="Open", command=self.open_alert)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_command(label="Save As...", command=self.save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.close_alert)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.toolmenu = tk.Menu(self.menubar, tearoff=0)
        self.toolmenu.add_command(label="Word count", command=self.word_count)
        self.menubar.add_cascade(label="Tools", menu=self.toolmenu)


        self.txt_input = tk.scrolledtext.ScrolledText(self.master, font=("Carlito", 12))
        self.txt_input.pack(expand=True, fill=tk.BOTH)

        self.master.config(menu=self.menubar)

TextEditor.new = functions.new
TextEditor.open = functions.open
TextEditor.open_alert = functions.open_alert
TextEditor.close_alert = functions.close_alert
TextEditor.delete_window = functions.delete_window
TextEditor.save = functions.save
TextEditor.save_as = functions.save_as
TextEditor.word_count = functions.word_count
