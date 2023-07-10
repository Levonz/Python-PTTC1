from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import *

textBoxPadx =110
textFont="Arial"
bgColor="#545454"
fgColor="#B346FF"

def them():{
    
}
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
name = StringVar()
nameTextBox = Entry(giaodien,width=50,textvariable=name)
nameTextBox.grid(row=1,column=0,sticky=W,padx=textBoxPadx)
#Tuoi
ageLabel = Label(giaodien,text="Tuổi:",fg=fgColor,bg=bgColor,font=(textFont,12))
ageLabel.grid(row=2,column=0,sticky=W)
#Tuoi textbox
age = IntVar()
ageTextBox = Entry(giaodien,width=50,textvariable=age)
ageTextBox.grid(row=2,column=0,sticky=W,padx=textBoxPadx)
#QueQuan
ageLabel = Label(giaodien,text="Quê Quán:",fg=fgColor,bg=bgColor,font=(textFont,12))
ageLabel.grid(row=3,column=0,sticky=W)
#QueQuan textbox
country = StringVar()
countryTextBox = Entry(giaodien,width=50,textvariable=country)
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
information = StringVar()
informationTextBox = Entry(giaodien,width=50,textvariable=information)
informationTextBox.grid(row=5,column=0,sticky=W,padx=textBoxPadx)
#Diem Tieng Anh
englishLabel = Label(giaodien,text="Tiếng Anh:",fg=fgColor,bg=bgColor,font=(textFont,12))
englishLabel.grid(row=6,column=0,sticky=W)
#Diem Tieng Anh textbox
english = StringVar()
englishTextBox = Entry(giaodien,width=50,textvariable=english)
englishTextBox.grid(row=6,column=0,sticky=W,padx=textBoxPadx)

#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command=them)
addButton.grid(row=7,sticky='W',padx=0,pady=5)
#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command=them)
addButton.grid(row=7,sticky='W',padx=120)
#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command=them)
addButton.grid(row=8,sticky='W',padx=0,pady=5)
#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command=them)
addButton.grid(row=8,sticky='W',padx=120)

#Scrolled
scrolled = ScrolledText(giaodien,width = 50, height = 10)
scrolled.grid(column=0,row=9,pady=5)
#Them hoc Vien Button
addButton = Button(giaodien,text='Thêm học viên',font=(textFont,12),fg=fgColor,bg=bgColor,command=them)
addButton.grid(row=10,sticky='W',padx=120)




giaodien.mainloop()