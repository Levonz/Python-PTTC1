import tkinter as tk
from tkinter import ttk

def button_function():
    # get the content of the entry
    entry_text = entry.get()
    
    #update the label
    # label.configure(text = "some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"

def ex_button_function():
    label["text"] = "some text"
    entry["state"] = "enabled"

# window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("200x100")

# widgets
label = ttk.Label(master = window, text = "some text")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window,text = "change", command = button_function)
button.pack()

ex_button = ttk.Button(master = window,text = "again", command = ex_button_function)
ex_button.pack()

# run
window.mainloop()