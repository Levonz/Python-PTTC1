#C R U D
#Create Read Update Delete

from PTTC1DinhNghia import PTTC1

class QuanLyHocVien:
    list_hoc_vien =[]
    def Them_Hoc_Vien(self):
        n = int(input("Nhập số lượng học viên: "))
        for i in range(len(QuanLyHocVien.list_hoc_vien),len(QuanLyHocVien.list_hoc_vien)+n):
            print('Nhập thông tin học viên mới: ')
            name= input('Tên: ')
            age = int(input('Tuổi: '))
            country = input('Quê quán:')
            lop = input('Lớp: ')
            diem_TA = float(input('Điểm Tiếng Anh:'))
            diem_tin = float(input('Điểm Tin học: '))
            hoc_vien = PTTC1(name,age,country,lop,diem_TA,diem_tin)
            hoc_vien.id = i+1
            if (diem_TA+diem_tin)/2 >5:
                hoc_vien.xep_loai = 'Giỏi'
            else:
                hoc_vien.xep_loai = 'Yếu'
            self.list_hoc_vien.append(hoc_vien)
            
    
    def Sua_Thong_Tin_Hoc_Vien(t):
        for i in QuanLyHocVien.list_hoc_vien:
            c=0
            if i.id ==t:
                c=1
                i.name = input('Nhập tên: ')   
                i.age = int(input('Nhập tuổi: '))  
                i.country = input('Quê quán:')
                i.lop = input('Lớp: ')
                i.diem_TA = float(input('Điểm Tiếng Anh:'))
                i.diem_tin = float(input('Điểm Tin học: '))
        if c==0:
            print('Không tìm thấy ID')
    
    def Xoa_Hoc_Vien(t):
        c=0
        for i in QuanLyHocVien.list_hoc_vien:
            if i.id == t:
                c=1
                QuanLyHocVien.list_hoc_vien.remove(i)
        if c==0:
            print('Không tìm thấy ID')          
        
    def Hien_Thi_Hoc_Vien():
        print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(
            'id','Name','Age','Country','Class','English','Tin','Xếp loại'))
        for i in QuanLyHocVien.list_hoc_vien:
            print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(
                i.id,i.name,i.age,i.country,i.lop,i.diem_TA,i.diem_tin,i.xep_loai))
        

# test = QuanLyHocVien()
# test.Them_Hoc_Vien()
# test.Hien_Thi_Hoc_Vien()
# t= int(input('Nhập id muốn sửa: '))
# test.Sua_Thong_Tin_Hoc_Vien(t)
# test.Hien_Thi_Hoc_Vien()
# t= int(input('Nhập id muốn xóa: '))
# test.Xoa_Hoc_Vien(t)
# test.Hien_Thi_Hoc_Vien()
#Yêu cầu
# tạo id tự động
# tính điểm tb 
# xep loại: Trung bình >5: giỏi <5: yếu
#in ra cột id và Xếp loại

#sửa thông tin học viên
#xóa thông tin học viên