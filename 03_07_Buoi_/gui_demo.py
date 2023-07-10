import tkinter
from tkinter.ttk import Combobox
from tkinter.scrolledtext import *


def cong():
    tong = int(giatri1.get())+int(giatri2.get())
    giatri3.set(tong)
    
def tru():
    hieu = int(giatri1.get())-int(giatri2.get())
    giatri3.set(hieu)
    
def nhan():
    tich = float(giatri1.get())*float(giatri2.get())
    giatri3.set(tich)
    
def chia():
    try:
        thuong = float(giatri1.get())/float(giatri2.get())
        giatri3.set(thuong)
    except ZeroDivisionError:
        giatri3.set(0)
        print('Số chia không thể bằng 0')
    
#Khung giao dien
giaodien = tkinter.Tk()
giaodien.title('Quản lý nhân viên') #Tên Chương trình
giaodien.geometry('500x200') #Kích thước khung

label3 = tkinter.Label(giaodien,text= 'Tinh tong 2 so',fg='black',bg='white')
label3.grid(column=1,row=0)
#Dong 1 Nhap so thu 1
label1 = tkinter.Label(giaodien,text= 'So thu nhat:',fg='black',bg='white')
label1.grid(column=0,row=1,sticky = 'W',padx=10)

giatri1 = tkinter.IntVar()
textbox1 = tkinter.Entry(giaodien,width='15',textvariable=giatri1)
textbox1.grid(column=1,row=1)

#Dong 2 Nhap so thu 2
label2 = tkinter.Label(giaodien,text= 'So thu hai:  ',fg='black',bg='white')
label2.grid(column=0,row=2,sticky = 'W',padx=10)

giatri2 = tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien,width='15',textvariable=giatri2)
textbox2.grid(column=1,row=2)

#Nut Tong
tongButton = tkinter.Button(giaodien,text='Tính tổng',fg='black',bg='yellow',command=cong)
tongButton.grid(column=0,row=3,sticky='W',padx=15)
#Nut Hieu
hieuButton = tkinter.Button(giaodien,text='Tính hiệu',fg='black',bg='yellow',command=tru)
hieuButton.grid(column=1,row=3,sticky='W',padx=15)
#Nut Nhan
nhanButton = tkinter.Button(giaodien,text='Tính tích',fg='black',bg='yellow',command=nhan)
nhanButton.grid(column=2,row=3,sticky='W',padx=15)
# Nut Chia
chiaButton = tkinter.Button(giaodien,text='Tính thương',fg='black',bg='yellow',command=chia)
chiaButton.grid(column=3,row=3,sticky='W',padx=15)


giatri3 = tkinter.IntVar()
textbox3 = tkinter.Entry(giaodien,width='15',textvariable=giatri3)
textbox3.grid(column=1,row=4)

combobox = Combobox(giaodien)
combobox['values'] = [1,2,3,'text']
combobox.grid(column=3,row=5)

scrolled = ScrolledText(giaodien,width = 20, height = 10)
scrolled.grid(column=3,row=6)

giaodien.mainloop()