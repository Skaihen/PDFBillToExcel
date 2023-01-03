import tkinter as tk
import os

from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory


def open_pdf():
    # Open a file for editing
    filePath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if not filePath:
        return
    os.mkdir(filePath + "")
    window.title(f"PDF Bill to Excel - {filePath}")


def open_folder():
    # Open a folder for editing
    folderPath = askdirectory(
        initialfile=None
    )
    if not folderPath:
        return
    window.title(f"PDF Bill to Excel - {folderPath}")


window = tk.Tk()
window.title("PDF Bill to Excel")

window.rowconfigure(0, minsize=400)
window.columnconfigure(1, minsize=400)

treeview = ttk.Treeview()
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open_folder = tk.Button(
    frm_buttons, text="Open Folder", command=open_folder)
btn_open = tk.Button(frm_buttons, text="Open Folder", command=open_folder)
btn_close = tk.Button(frm_buttons, text="Exit", command=window.destroy)

btn_open_folder.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_close.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
treeview.grid(row=0, column=1, sticky="nsew")

window.minsize(width=400, height=400)
treeview.pack()
window.mainloop()
