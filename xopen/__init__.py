""" Launch xdg-open with the provided file locations
"""
from tkinter import Tk
from tkinter.ttk import Entry
from subprocess import run


def main():
    """Prepare the GUI
    And launch it
    """
    window = Tk(className='xopen-file')
    window.title("xopen-file")
    window.configure(background='white')
    window.minsize(100, 10)
    window.resizable(False, False)

    text_box = Entry(window, width=30)
    text_box.bind('<Return>', lambda e: handle_entry(window, text_box))
    text_box.bind('<KP_Enter>', lambda e: handle_entry(window, text_box))
    text_box.pack()

    window.mainloop()


def handle_entry(root, box):
    """ destroy the window and launch xdg-open
    """
    file_location = box.get().strip()
    root.destroy()
    run(['xdg-open', file_location])
