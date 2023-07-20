import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import *
import connectSql

ketnoi = connectSql.getConnection()
dulieu = ketnoi.cursor()

# def
def getalldata():
    sql ='SELECT * FROM quan_ly_nhan_vien.nhanvien'
    dulieu.execute(sql)
    ketqua = dulieu.fetchall()
    return(ketqua)

def tinhLuong():
    ketqua = getalldata()
    newList = []
    for i in ketqua:
        luong = i[-1]*300000
        if i[-2]=='TP':
            luong = luong*1.6
        elif i[-2]=='GD':
            luong = luong*2
        i=list(i)
        i.append(luong)
        i=tuple(i)
        newList.append(i)
    return(newList)

def sinhId():
    ketqua=tinhLuong()
    TP = 1
    GD = 1
    NV = 1
    newList=[]
    for i in ketqua:
        id = i[0]
        if i[-3] == 'TP':
            i = list(i)
            newId=i[-3]+str(TP)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            TP+=1
        elif i[-3] == 'NV':
            i = list(i)
            newId=i[-3]+str(NV)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            NV+=1
        elif i[-3] == 'GD':
            i = list(i)
            newId=i[-3]+str(GD)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            GD+=1
    return(newList)

def show():
    ketqua = sinhId()
    idEntry["state"] = "disable"
    scrolled.delete("1.0","end")
    fRow=('{:<5} {:<13} {:<3} {:<5} {:<10} {:<4} {:<4} {:^15}'.format(
            'ID','Name','Age','Sex','Country','Role','Work','Salary'))
    scrolled.insert("end",fRow+"\n")
    for i in ketqua:
        row=('{:<5} {:<13} {:<3} {:<5} {:<10} {:<4} {:<4} {:>13,.0f} VND'.format(
            i[-1],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        scrolled.insert("end",row+"\n")
        
def add():
    name = nameInput.get()
    age = ageInput.get()
    sex = sexCombobox.get()
    country = countryInput.get()
    role = roleCombobox.get()
    workDays = workDaysInput.get()
    dulieu.execute("INSERT INTO quan_ly_nhan_vien.nhanvien(`Name`,Age,sex,Country,Chucvu,Songaylam) VALUES('{}','{}','{}','{}','{}',{})"
                    .format(name,age,sex,country,role,workDays))
    ketnoi.commit()
    addNotice.set("Da Them")
    
def change():
    ketqua = sinhId()
    idEntry["state"] = "enable"
    addNotice.set("Nhap ID --->")
    newId = idInput.get()
    exist = False
    for i in ketqua:
        if i[-1] == newId:
            id = i[0]
            exist = True
            break
    if exist == True:
        name = nameInput.get()
        age = ageInput.get()
        sex = sexCombobox.get()
        country = countryInput.get()
        role = roleCombobox.get()
        workDays = workDaysInput.get()
        sql ="UPDATE quan_ly_nhan_vien.nhanvien SET `Name` = %s,Age = %s,Sex =%s,Country = %s,Chucvu = %s,Songaylam = %s WHERE Id = %s"
        dulieu.execute(sql,(name,age,sex,country,role,workDays,id))
        ketnoi.commit()
        
    else:
        addNotice.set('Id không tồn tại!')
    
def delete():
    ketqua = sinhId()
    idEntry["state"] = "enable"
    addNotice.set("Nhap ID --->")
    newId = idInput.get()
    exist = False
    for i in ketqua:
        if i[-1] == newId:
            id = i[0]
            exist = True
            break
    if exist == True:
        sql = "DELETE FROM quan_ly_nhan_vien.nhanvien WHERE Id = '{}'".format(id)
        dulieu.execute(sql)
        ketnoi.commit()
    else:
        addNotice.set('Id không tồn tại!')

def connectCheck():
    if ketnoi.is_connected()==True:
        connectCheck.set('Kết nối thành công!')
    else:
        connectCheck.set('Kết nối không thành công')
        
def sort():
    ketqua=sinhId()
    listName = []
    for i in ketqua:
        listName.append(i[1].split()[-1])       
    listName.sort()
    scrolled.delete("1.0","end")
    fRow=('{:<5} {:<13} {:<3} {:<5} {:<10} {:<4} {:<4} {:^15}'.format(
            'ID','Name','Age','Sex','Country','Role','Work','Salary'))
    scrolled.insert("end",fRow+"\n")
    for j in listName:
        for i in ketqua:
            if i[1].split()[-1] == j:
                row=('{:<5} {:<13} {:<3} {:<5} {:<10} {:<4} {:<4} {:>13,.0f} VND'.format(
                        i[-1],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                scrolled.insert("end",row+"\n")

# window
window = tk.Tk()
window.title("Quan Ly Nhan Vien")
window.geometry("650x600")

# grid define
window.columnconfigure((0,1,2,3,4),weight = 1,uniform = "a")
window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight = 0)

# widgets
titleLabel = ttk.Label(window, text = "CHUONG TRINH QUAN LY NHAN VIEN")
nameLabel = ttk.Label(window, text = "Ten:")
ageLabel = ttk.Label(window, text = "Tuoi:")
sexLabel = ttk.Label(window, text = "Gioi Tinh:")
countryLabel = ttk.Label(window, text = "Que Quan:")
roleLabel = ttk.Label(window, text = "Chuc Vu:")
workDaysLabel = ttk.Label(window, text = "So Ngay Lam:")

nameInput = tk.StringVar()
ageInput = tk.StringVar()
countryInput = tk.StringVar()
roleInput = tk.StringVar()
workDaysInput = tk.StringVar()

nameEntry = ttk.Entry(window, textvariable = nameInput)
ageEntry = ttk.Entry(window, textvariable = ageInput)
sexCombobox = ttk.Combobox(window)
sexCombobox['values'] = ['Nam','Nu','Khac']
countryEntry = ttk.Entry(window, textvariable = countryInput)
roleCombobox = ttk.Combobox(window)
roleCombobox['values'] = ['NV','TP','GD']
workDaysEntry = ttk.Entry(window, textvariable = workDaysInput)

addButton = ttk.Button(window, text = "Them Nhan Vien",command = add)
showButton = ttk.Button(window, text = "Hien Thi Nhan Vien",command=show)
deleteButton = ttk.Button(window, text = "Xoa Nhan Vien",command = delete)
changeButton = ttk.Button(window, text = "Sua Nhan Vien",command = change)
sortButton = ttk.Button(window, text = "Sap Xep Theo Ten",command = sort)

idInput = tk.StringVar()
idEntry = ttk.Entry(window, textvariable = idInput, state = "disable")

addNotice = tk.StringVar()
addNoticeLabel = tk.Label(window, textvariable = addNotice)

scrolled = ScrolledText(window, width = 50, height = 15)

checkConnectButton = ttk.Button(window, text = "Kiem tra Ket Noi",command = connectCheck)
connectCheck = tk.StringVar()
connectCheckLabel = ttk.Label(window, textvariable = connectCheck)


# grid
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

addButton.grid(row = 7, column = 0, sticky = "we",padx=5,pady = 5)
showButton.grid(row = 7, column = 1, sticky = "we",padx=5,pady = 5)
idEntry.grid(row = 8, column = 3, sticky = "we",padx=5,pady = 5)
deleteButton.grid(row = 7, column = 2, sticky = "we",padx=5,pady = 5)
changeButton.grid(row = 7, column = 3, sticky = "we",padx=5,pady = 5)
sortButton.grid(row = 8, column = 0, sticky = "we",padx=5,pady = 5)
addNoticeLabel.grid(row = 8, column = 2, sticky = "we",pady = 5)

scrolled.grid(row = 9,column= 0, columnspan = 5, sticky = "we", padx = 10,pady = 5)

checkConnectButton.grid(row = 10,column = 2, sticky = "we",pady = 5)
connectCheckLabel.grid(row = 11, column = 2,pady = 5)

# run
window.mainloop()