import tkinter as tk
from tkinter import ttk
import random


def randomKetQua():
    ketQua =[0,1,2,3,4,5,6,7]
    ketQua[0] = random.randint(00000,99999)
    ketQua[1] = random.randint(00000,99999)
    ketQua[2] = [random.randint(00000,99999),random.randint(00000,99999)]
    ketQua[3] = [random.randint(00000,99999),random.randint(00000,99999),random.randint(00000,99999)
                 ,random.randint(00000,99999),random.randint(00000,99999),random.randint(00000,99999)]
    ketQua[4] = [random.randint(0000,9999),random.randint(0000,9999)
                 ,random.randint(0000,9999),random.randint(0000,9999)]
    ketQua[5] = [random.randint(0000,9999),random.randint(0000,9999),random.randint(0000,9999)
                 ,random.randint(0000,9999),random.randint(0000,9999),random.randint(0000,9999)]
    ketQua[6] = [random.randint(000,999),random.randint(000,999),random.randint(000,999)]
    ketQua[7] = [random.randint(00,99),random.randint(00,99)
                 ,random.randint(00,99),random.randint(00,99)]
    text.delete("1.0","end")
    text.insert("end","{:20} {:^30} \n".format("Giai DB:",ketQua[0]))
    text.insert("end","{:20} {:^30} \n".format("Giai Nhat:",ketQua[1]))
    text.insert("end","{:20} {:^30} \n".format("Giai Nhi:",str(ketQua[2][0])+" "+str(ketQua[2][1])))
    text.insert("end","{:20} {:^30} \n".format("Giai Ba:",str(ketQua[3][0])+" "+str(ketQua[3][1])+" "+str(ketQua[3][2])))
    text.insert("end","{:20} {:^30} \n".format("",str(ketQua[3][3])+" "+str(ketQua[3][4])+" "+str(ketQua[3][5])))
    text.insert("end","{:20} {:^30} \n".format("Giai Bon:",str(ketQua[4][0])+" "+str(ketQua[4][1])+" "+str(ketQua[4][2])+" "+
                                               str(ketQua[4][3])))
    text.insert("end","{:20} {:^30} \n".format("Giai Nam:",str(ketQua[5][0])+" "+str(ketQua[5][1])+" "+str(ketQua[5][2])))
    text.insert("end","{:20} {:^30} \n".format("",str(ketQua[5][3])+" "+str(ketQua[5][4])+" "+str(ketQua[5][5])))
    text.insert("end","{:20} {:^30} \n".format("Giai Sau:",str(ketQua[6][0])+" "+str(ketQua[6][1])+" "+str(ketQua[6][2])))
    text.insert("end","{:20} {:^30} \n".format("Giai Bay:",str(ketQua[7][0])+" "+str(ketQua[7][1])+" "+str(ketQua[7][2])+" "+
                                               str(ketQua[7][3])))
    return ketQua

def choiDe():
    so = soDe.get()
    diem = int(soDiemDe.get())
    tienConLai = tien.get()
    ketQua = randomKetQua()
    if (so) == str(ketQua[0]%100):
        tien.set(tienConLai+diem*23000)
    else:
        tien.set(tienConLai-diem*23000)

def choiLo():
    so = soLo.get()
    diem = int(soDiemLo.get())
    tienConLai = tien.get()
    ketQua = randomKetQua()
    ketQuaLo = []
    ketQuaLo.append(str(ketQua[1]%100))
    ketQuaLo.append(str(ketQua[2][0]%100))
    ketQuaLo.append(str(ketQua[2][1]%100))
    
    ketQuaLo.append(str(ketQua[3][0]%100))
    ketQuaLo.append(str(ketQua[3][1]%100))
    ketQuaLo.append(str(ketQua[3][2]%100))
    ketQuaLo.append(str(ketQua[3][3]%100))
    ketQuaLo.append(str(ketQua[3][4]%100))
    ketQuaLo.append(str(ketQua[3][5]%100))
    
    ketQuaLo.append(str(ketQua[4][0]%100))
    ketQuaLo.append(str(ketQua[4][1]%100))
    ketQuaLo.append(str(ketQua[4][2]%100))
    ketQuaLo.append(str(ketQua[4][3]%100))
    
    ketQuaLo.append(str(ketQua[5][0]%100))
    ketQuaLo.append(str(ketQua[5][1]%100))
    ketQuaLo.append(str(ketQua[5][2]%100))
    ketQuaLo.append(str(ketQua[5][3]%100))
    ketQuaLo.append(str(ketQua[5][4]%100))
    ketQuaLo.append(str(ketQua[5][5]%100))
     
    ketQuaLo.append(str(ketQua[6][0]%100))
    ketQuaLo.append(str(ketQua[6][1]%100))
    ketQuaLo.append(str(ketQua[6][2]%100))
    
    ketQuaLo.append(str(ketQua[7][0]%100))
    ketQuaLo.append(str(ketQua[7][1]%100))
    ketQuaLo.append(str(ketQua[7][2]%100))
    ketQuaLo.append(str(ketQua[7][3]%100))
    
    for i in ketQuaLo:
        if so == i:
            tien.set(tienConLai+diem*1000)   
        else:
            tien.set(tienConLai-diem*1000)
    


# window
window = tk.Tk()
window.title("Tro Choi Lo De")
window.geometry("800x1000")


# widgets
titleLabel = ttk.Label(master = window, text ="Tro Choi Lo de")
titleLabel.pack(pady = 5)

loLabel = ttk.Label(window, text = "I.Choi lo")
loLabel.pack(pady = 5)

frame1 = ttk.Frame(window)
label1 = ttk.Label(frame1, text = "Chon so:")
soDe = tk.StringVar()
entry1 = ttk.Entry(frame1,textvariable = soDe)
label2 = ttk.Label(frame1, text = "Danh may diem:")
soDiemDe = tk.StringVar()
entry2 = ttk.Entry(frame1, textvariable = soDiemDe)
label1.pack(side = "left",padx =10)
entry1.pack(side = "left")
label2.pack(side = "left",padx =10)
entry2.pack(side = "left")
frame1.pack(pady = 5)

frame11 = ttk.Frame(window)
choiButton = ttk.Button(frame11,text = "Choi di dung so", command = choiDe)
label3 = ttk.Label(frame11, text = "1 diem = 23.000 VND")
choiButton.pack(side = "left",padx =10)
label3.pack(side = "left")
frame11.pack(pady = 5)


deLabel = ttk.Label(window, text = "II.Choi de")
deLabel.pack(pady = 5)

# frame 2
frame2 = ttk.Frame(window)
label4 = ttk.Label(frame2, text = "Chon so:")
soLo = tk.StringVar()
entry3 = ttk.Entry(frame2,textvariable = soLo)
label5 = ttk.Label(frame2, text = "Danh may diem:")
soDiemLo = tk.StringVar()
entry4 = ttk.Entry(frame2,textvariable = soDiemLo)
label4.pack(side = "left",padx =10)
entry3.pack(side = "left")
label5.pack(side = "left",padx =10)
entry4.pack(side = "left")
frame2.pack(pady = 5)

frame22 = ttk.Frame(window)
choiButton1 = ttk.Button(frame22,text = "Choi di dung so",command = choiLo)
label6 = ttk.Label(frame22, text = "1 diem = 1.000 VND")
choiButton1.pack(side = "left",padx =10)
label6.pack(side = "left")
frame22.pack(pady = 5)

text = tk.Text(window)
text.pack()

tien = tk.IntVar()
tien.set(1000000)
tongTienLabel = ttk.Label(window,text = "Tong tien: 1.000.000 VND")
tongTienLabel.pack(pady = 5)

frame33 = ttk.Frame(window)
tienConLaiLabel = ttk.Label(frame33,text = "So tien con lai")
tienConLaiLabel.pack(side = "left",padx =10)
tienConLaiEntry = ttk.Entry(frame33,textvariable = tien)
tienConLaiEntry.pack(side = "left")
frame33.pack(pady = 5)

# run
window.mainloop()