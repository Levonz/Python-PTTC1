import tkinter as tk
import tkkbootstrap as ttk
from tkinter import ttk

def button_function():
    print("a button was pressed")

def hello():
    print("hello")

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master = window, text = "This is a test")
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk label
label1 = ttk.Label(master = window, text = "my label")
label1.pack()

# ttk button
button1 = ttk.Button(master = window, text = "Hello", command = hello)
button1.pack()

# ttk button
button = ttk.Button(master = window, text = "A Button", command = button_function)
button.pack()

# run
window.mainloop()