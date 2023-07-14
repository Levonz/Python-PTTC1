import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import *

import ConnectSQL
import mysql.connector

ketnoi = ConnectSQL.getConnection()
dulieu = ketnoi.cursor()

# configure
textBoxPadx =110
textFont="Helvetica"
bgColor="white"
fgColor="black"

# function
def connectCheck():
    if ketnoi.is_connected()==True:
        connectVar.set('Kết nối thành công!')
    else:
        connectVar.set('Kết nối không thành công')
def add():
    name = nameInput.get()
    age = ageInput.get()
    country = countryInput.get()
    sex = sexCombobox.get()
    english = englishInput.get()
    information = informationInput.get()
    dulieu.execute("INSERT INTO quan_ly_hoc_vien.hocvien(`Name`,Age,Country,Sex,English,Information) VALUES('{}',{},'{}','{}',{},{})".format(name,age,country,sex,english,information))
    ketnoi.commit()
    addVar.set('Đã thêm')
    
def show():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    scrolled.delete("1.0","end")
    str1 = ('{:<2}|{:<13}|{:<3}|{:<10}|{:<5}|{:<11}|{:<5}'.format(
            'Id','Name','Age','Country','Sex','Information','English'))
    scrolled.insert("end",str1 + "\n")
    for i in ketqua:
        str2 = ('{:<2}|{:<13}|{:<3}|{:<10}|{:<5}|{:<11}|{:<5}'.format(
            i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        scrolled.insert("end",str2 + "\n")

def delete():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    exist = False
    idEntry["state"]= "enabled"
    idLabelInput.set("Nhập Id")
    id = int(idEntry.get())
    for i in ketqua:
        if i[0] == id:
            exist = True
            break
    if exist == True:
        sql = "DELETE FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(id)
        dulieu.execute(sql)
        ketnoi.commit()
    else:
        idLabelInput.set("Id không tồn tại")

def change():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    exist = False
    idEntry["state"]= "enabled"
    idLabelInput.set("Nhập Id")
    id = int(idEntry.get())
    for i in ketqua:
        if i[0] == id:
            exist = True
            break
    if exist == True:
        name = nameInput.get()
        age = ageInput.get()
        country = countryInput.get()
        sex = sexCombobox.get()
        english = englishInput.get()
        information = informationInput.get()
        sql ="UPDATE quan_ly_hoc_vien.hocvien SET `Name` = %s,Age = %s,Country = %s,English = %s,Information = %s WHERE Id = %s"
        dulieu.execute(sql,(name,age,country,english,information,id))
        ketnoi.commit()
    else:
        idLabelInput.set("Id không tồn tại")

# window
window = tk.Tk()
window.title('Quan Ly Hoc Vien')  #Tên Chương trình
window.geometry('500x500')        #Kích thước khung

# title
titleLabel = ttk.Label(master = window,text="CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN")
titleLabel.pack()

# name
nameInputFrame = ttk.Frame(master = window)  
nameInput = tk.StringVar()
nameLabel = ttk.Label(master = nameInputFrame,text="Tên:")
nameEntry = ttk.Entry(master = nameInputFrame,textvariable=nameInput)
nameLabel.pack(side = "left", padx = 10)
nameEntry.pack(side = "left")
nameInputFrame.pack(anchor = "nw", pady = 5)
# age
ageInputFrame = ttk.Frame(master = window)
ageInput = tk.IntVar()
ageLabel = ttk.Label(master = ageInputFrame,text="Tuổi:")
ageEntry = ttk.Entry(master = ageInputFrame,textvariable=ageInput)
ageLabel.pack(side = "left", padx = 10)
ageEntry.pack(side = "left")
ageInputFrame.pack(anchor = "nw", pady = 5)
# country
countryInputFrame = ttk.Frame(master = window)
countryInput = tk.StringVar()
countryLabel = ttk.Label(master = countryInputFrame,text="Quê Quán:")
countryEntry = ttk.Entry(master = countryInputFrame,textvariable=countryInput)
countryLabel.pack(side = "left", padx = 10)
countryEntry.pack(side = "left")
countryInputFrame.pack(anchor = "nw", pady = 5)
# sex
sexInputFrame = ttk.Frame(master = window)
sexLabel = ttk.Label(master = sexInputFrame,text="Giới tính:")
sexCombobox = ttk.Combobox(master = sexInputFrame)
sexCombobox['values'] = ['Male','Female','Others']
sexLabel.pack(side = "left", padx = 10)
sexCombobox.pack(side = "left")
sexInputFrame.pack(anchor = "nw", pady = 5)
# information
informationInputFrame = ttk.Frame(master = window)
informationInput = tk.StringVar()
informationLabel = ttk.Label(master = informationInputFrame,text="Tin học:")
informationEntry = ttk.Entry(master = informationInputFrame,textvariable=informationInput)
informationLabel.pack(side = "left", padx = 10)
informationEntry.pack(side = "left")
informationInputFrame.pack(anchor = "nw", pady = 5)
# english
englishInputFrame = ttk.Frame(master = window)
englishInput = tk.StringVar()
englishLabel = ttk.Label(master = englishInputFrame,text="Tiếng Anh:")
englishEntry = ttk.Entry(master = englishInputFrame,textvariable=englishInput)
englishLabel.pack(side = "left", padx = 10)
englishEntry.pack(side = "left")
englishInputFrame.pack(anchor = "nw", pady = 5)

# button

buttonGroup1 = ttk.Frame(master = window)
# add button
addButton = ttk.Button(master = buttonGroup1,text='Thêm học viên',command = add)
addButton.pack(side = "left",padx = 15)
# show button
showButton = ttk.Button(master = buttonGroup1,text='Hiển thị học viên',command = show)
showButton.pack(side = "left",padx = 15)
# id entry
idInput = tk.StringVar()
idLabelInput = tk.StringVar()
idLabelInput.set("        ")
idLabel = ttk.Label(master = buttonGroup1,textvariable = idLabelInput)
idEntry = ttk.Entry(master = buttonGroup1,textvariable = idInput,state = "disabled")
idLabel.pack(side = "left")
idEntry.pack(side = "left")
buttonGroup1.pack(anchor = "nw", pady = 5)

buttonGroup2 = ttk.Frame(master = window)
# delete button
deleteButton = ttk.Button(master = buttonGroup2,text='Xóa học viên',command = delete)
deleteButton.pack(side = "left",padx = 15)
# change button
changeButton = ttk.Button(master = buttonGroup2,text='Sửa học viên',command = change)
changeButton.pack(side = "left")
# add notice lable
addVar = tk.StringVar()
addNoticeLabel = ttk.Label(master = window,textvariable=addVar)
addNoticeLabel.pack()
buttonGroup2.pack(anchor = "nw", pady = 5)

# scrolled
scrolled = ScrolledText(master = window,width = 58, height = 10)
scrolled.pack()

# check connect button
checkConnectButton = ttk.Button(master = window,text='Kiểm tra kết nối',command = connectCheck)
checkConnectButton.pack()
connectVar = tk.StringVar()
connectOutputLabel = ttk.Label(master = window,text='Kết nối thành công!',textvariable=connectVar)
connectOutputLabel.pack()

# run
window.mainloop()