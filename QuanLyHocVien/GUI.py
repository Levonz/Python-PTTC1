from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import *
import ConnectSQL
import mysql.connector

ketnoi = ConnectSQL.getConnection()
dulieu = ketnoi.cursor()

textBoxPadx =110
textFont="Helvetica"
bgColor="white"
fgColor="black"

def connectCheck():
    if ketnoi.is_connected()==True:
        connectOP.set('Kết nối thành công!')
    else:
        connectOP.set('Kết nối không thành công')
def them():
    name = nameI.get()
    age = ageI.get()
    country = countryI.get()
    english = englishI.get()
    information = informationI.get()
    dulieu.execute("INSERT INTO quan_ly_hoc_vien.hocvien(`Name`,Age,Country,English,Information) VALUES('{}',{},'{}',{},{})".format(name,age,country,english,information))
    ketnoi.commit()
    addOP.set('Đã thêm')

def hienThi():
    return
#Khung giao dien
giaodien = Tk()
giaodien.title('Quản lý học viên')  #Tên Chương trình
giaodien.geometry('500x500')        #Kích thước khung
giaodien.configure(bg=bgColor)      #Đổi màu BG

#CHUONG TRINH QUAN LY HOC VIEN
titleLabel = Label(giaodien,text="CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN",fg=fgColor,bg=bgColor,font=(textFont,14))
titleLabel.grid(row=0,column=0,padx=70)

#Ten
nameLabel = Label(giaodien,text="Tên:",fg=fgColor,bg=bgColor,font=(textFont,12))
nameLabel.grid(row=1,column=0,sticky=W)
#Ten textbox
nameI = StringVar()
nameTextBox = Entry(giaodien,width=50,textvariable=nameI)
nameTextBox.grid(row=1,column=0,sticky=W,padx=textBoxPadx)
#Tuoi
ageLabel = Label(giaodien,text="Tuổi:",fg=fgColor,bg=bgColor,font=(textFont,12))
ageLabel.grid(row=2,column=0,sticky=W)
#Tuoi textbox
ageI = IntVar()
ageTextBox = Entry(giaodien,width=50,textvariable=ageI)
ageTextBox.grid(row=2,column=0,sticky=W,padx=textBoxPadx)
#QueQuan
ageLabel = Label(giaodien,text="Quê Quán:",fg=fgColor,bg=bgColor,font=(textFont,12))
ageLabel.grid(row=3,column=0,sticky=W)
#QueQuan textbox
countryI = StringVar()
countryTextBox = Entry(giaodien,width=50,textvariable=countryI)
countryTextBox.grid(row=3,column=0,sticky=W,padx=textBoxPadx)
#GioiTinh
sexLabel = Label(giaodien,text="Giới tính:",fg=fgColor,bg=bgColor,font=(textFont,12))
sexLabel.grid(row=4,column=0,sticky=W)
#GioiTinh combobox
sexCombobox = Combobox(giaodien,width=47)
sexCombobox['values'] = ['Nam','Nữ','Khác']
sexCombobox.grid(row=4,column=0,sticky=W,padx=textBoxPadx)
#Tin Hoc
informationLabel = Label(giaodien,text="Tin học:",fg=fgColor,bg=bgColor,font=(textFont,12))
informationLabel.grid(row=5,column=0,sticky=W)
#Diem Tin textbox
informationI = StringVar()
informationTextBox = Entry(giaodien,width=50,textvariable=informationI)
informationTextBox.grid(row=5,column=0,sticky=W,padx=textBoxPadx)
#Diem Tieng Anh
englishLabel = Label(giaodien,text="Tiếng Anh:",fg=fgColor,bg=bgColor,font=(textFont,12))
englishLabel.grid(row=6,column=0,sticky=W)
#Diem Tieng Anh textbox
englishI = StringVar()
englishTextBox = Entry(giaodien,width=50,textvariable=englishI)
englishTextBox.grid(row=6,column=0,sticky=W,padx=textBoxPadx)

#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command =them)
addButton.grid(row=7,sticky='W',padx=0,pady=5)
#Them hoc Vien Button
addButton = Button(giaodien,text='Hiển thị học viên',font=(textFont,12),fg=fgColor,bg=bgColor)
addButton.grid(row=7,sticky='W',padx=120)
#Them hoc Vien Button
addButton = Button(giaodien,text='Xóa học viên',font=(textFont,12),fg=fgColor,bg=bgColor)
addButton.grid(row=8,sticky='W',padx=0,pady=5)
#Them hoc Vien Button
addButton = Button(giaodien,text='Sửa học viên',font=(textFont,12),fg=fgColor,bg=bgColor)
addButton.grid(row=8,sticky='W',padx=120)
#Da them
addOP=StringVar()
addOutput = Label(giaodien,font=(textFont,12),fg=fgColor,bg=bgColor
                      ,textvariable=addOP)
addOutput.grid(column=0,row=9)

#Scrolled
scrolled = ScrolledText(giaodien,width = 50, height = 10)
scrolled.grid(column=0,row=10,pady=5)
#Kiểm tra kết nối Button
addButton = Button(giaodien,text='Kiểm tra kết nối',font=(textFont,12),fg=fgColor,bg=bgColor
                   ,command = connectCheck)
addButton.grid(column=0,row=11)
connectOP = StringVar()
connectOutput = Label(giaodien,text='Kết nối thành công!',font=(textFont,12),fg=fgColor,bg=bgColor
                      ,textvariable=connectOP)
connectOutput.grid(column=0,row=12,pady=5)



giaodien.mainloop()