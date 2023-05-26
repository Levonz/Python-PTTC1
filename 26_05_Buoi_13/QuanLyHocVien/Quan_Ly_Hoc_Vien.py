#C R U D
#Create Read Update Delete

from PTTC1DinhNghia import PTTC1

class QuanLyHocVien:
    list_hoc_vien =[]
    dic = {}
    def Them_Hoc_Vien(self):
        n = int(input("Nhập số lượng học viên: "))
        for i in range(0,n):
            print('Nhập thông tin học viên thứ',i+1)
            name= input('Tên: ')
            age = int(input('Tuổi: '))
            country = input('Quê quán:')
            lop = input('Lớp: ')
            diem_TA = float(input('Điểm Tiếng Anh:'))
            diem_tin = float(input('Điểm Tin học: '))
            
            hoc_vien = PTTC1(name,age,country,lop,diem_TA,diem_tin)
            self.list_hoc_vien.append(hoc_vien)
            self.dic[i]=[hoc_vien]
            
    
            
    def Hien_Thi_Hoc_Vien(self):
        print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10}'.format(
            'id','Name','Age','Country','Class','English','Tin'))
        #for i in self.list_hoc_vien:
        #    print('{:<10} {:<7} {:<10} {:<10} {:<10} {:<10}'.format(
        #        i.name,i.age,i.country,i.lop,i.diem_TA,i.diem_tin))
        for key, value in self.dic.items():
            print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10}'.format(
                key,value[0].name,value[0].age,value[0].country,value[0].lop,
                  value[0].diem_TA,value[0].diem_tin))
test = QuanLyHocVien()
test.Them_Hoc_Vien()
test.Hien_Thi_Hoc_Vien()

#Yêu cầu
# tạo id tự động
# tính điểm tb 
# xep loại: Trung bình >5: giỏi <5: yếu
#in ra cột id và Xếp loại

#sửa thông tin học viên
#xóa thông tin học viên