#Định nghĩa class PTTC1 gồm các thuộc tính: Tên, tuổi, quê quán, lớp, điểm TA, 
#điểm Tin học
#Nhập số lượng học viên
#Nhập tay các thông tin cho học viên
#Show ra danh sách lớp PTTC1
#Nâng cao: Show theo kiểu table

class PTTC1():
    def __init__(self,name,age,country,lop,diem_TA,diem_tin):
        self.name = name
        self.age = age
        self.country = country
        self.lop = lop
        self.diem_TA = diem_TA
        self.diem_tin =diem_tin

list_hoc_vien =[]
n = int(input("Nhập số lượng học viên: "))
for i in range(0,n):
    print('Nhập thông tin học viên thứ',i+1)
    t = PTTC1(input('Tên: '),int(input('Tuổi: ')),input('Quê quán:')
              ,input('Lớp: '),input('Điểm Tiếng Anh:')
              ,input('Điểm Tin học: '))
    list_hoc_vien.append(t)
for i in list_hoc_vien:
    print(i.name,i.age,i.country,i.lop,i.diem_TA,i.diem_tin)
    