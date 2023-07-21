import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
              
        # widgets
        self.inputFrame = InputFrame(self)      
              
        # rung      
        self.mainloop()
        
class InputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky = "news")

        self.create_widgets()
        
    def create_widgets(self):
        titleLabel = ttk.Label(self, text = "CHUONG TRINH QUAN LY NHAN VIEN")
        nameLabel = ttk.Label(self, text = "Ten:")
        ageLabel = ttk.Label(self, text = "Tuoi:")
        sexLabel = ttk.Label(self, text = "Gioi Tinh:")
        countryLabel = ttk.Label(self, text = "Que Quan:")
        roleLabel = ttk.Label(self, text = "Chuc Vu:")
        workDaysLabel = ttk.Label(self, text = "So Ngay Lam:")

        nameInput = tk.StringVar()
        ageInput = tk.StringVar()
        countryInput = tk.StringVar()
        roleInput = tk.StringVar()
        workDaysInput = tk.StringVar()

        nameEntry = ttk.Entry(self, textvariable = nameInput)
        ageEntry = ttk.Entry(self, textvariable = ageInput)
        sexCombobox = ttk.Combobox(self)
        sexCombobox['values'] = ['Nam','Nu','Khac']
        countryEntry = ttk.Entry(self, textvariable = countryInput)
        roleCombobox = ttk.Combobox(self)
        roleCombobox['values'] = ['NV','TP','GD']
        workDaysEntry = ttk.Entry(self, textvariable = workDaysInput)
        
        self.columnconfigure((0,1,2,3,4),weight = 1,uniform = "a")
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight = 0)
        
        titleLabel.grid(row = 0, column = 1,columnspan=3, sticky = "ns",pady = 5)
        nameLabel.grid(row = 1, column = 0, sticky = "w", padx =10,pady = 5)
        nameEntry.grid(row =1, column = 1, columnspan = 3, sticky = "we",pady = 5)
        ageLabel.grid(row = 2, column = 0, sticky = "w", padx =10,pady = 5)
        ageEntry.grid(row = 2, column = 1, columnspan = 3, sticky = "we",pady = 5)
        sexLabel.grid(row = 3, column = 0, sticky = "w", padx =10,pady = 5)
        sexCombobox.grid(row = 3, column = 1, columnspan = 3, sticky = "we",pady = 5)
        countryLabel.grid(row = 4, column = 0, sticky = "w", padx =10,pady = 5)
        countryEntry.grid(row = 4, column = 1, columnspan = 3, sticky = "we",pady = 5)
        roleLabel.grid(row = 5, column = 0, sticky = "w", padx =10,pady = 5)
        roleCombobox.grid(row = 5, column = 1, columnspan = 3, sticky = "we",pady = 5)
        workDaysLabel.grid(row = 6, column = 0, sticky = "w", padx =10,pady = 5)
        workDaysEntry.grid(row = 6, column = 1, columnspan = 3, sticky = "we",pady = 5)


App("Quan Ly Nhan Vien", (600,600))