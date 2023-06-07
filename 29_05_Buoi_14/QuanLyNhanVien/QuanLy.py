from models import nhan_vien

class QuanLyNhanVien:
    list_nhan_vien =[]
    def them(self):
        n = int(input('Nhap so luong nhan vien: '))
        for i in range(1,n+1):
            print('Nhap thong tin nhan vien: ')
            ten = input('Ten: ')
            tuoi = int(input('Tuoi: '))
            queQuan = input('Que quan: ')
            chucVu = input('Chuc Vu TP, NV, GD: ')
            chamCong = int(input('So ngay lam viec: '))
            if chucVu == 'TP':
                luong = 300*chamCong*1.6
            elif chucVu == 'GD':
                luong = 300*chamCong*2
            else:
                luong = 300*chamCong
            
            nhanVien = nhan_vien(ten,tuoi,queQuan,chucVu,chamCong,luong)
            
            c=1
            if chucVu == 'NV':
                nhanVien.id = chucVu+str(c)
                c+=1
            elif chucVu == 'GD':
                nhanVien.id = chucVu+str(c)
            else:
                nhanVien.id = chucVu+str(c)
            self.list_nhan_vien.append(nhanVien)
            
    def sua(self,t):
        for i in self.list_nhan_vien:
            c=0
            if i.id ==t:
                c=1
                i.ten = input('Nhập tên: ')   
                i.tuoi = int(input('Nhập tuổi: '))  
                i.queQuan = input('Quê quán:')
                i.chucVu = input('Chuc vu: ')
                i.chamCong = float(input('So ngay lam: '))
                if chucVu == 'TP':
                    luong = 300*chamCong*1.6
                elif chucVu == 'GD':
                    luong = 300*chamCong*2
                else:
                    luong = 300*chamCong
        if c==0:
            print('Không tìm thấy ID')
    
    def xoa(self,t):
        c=0
        for i in self.list_nhan_vien:
            if i.id == t:
                c=1
                self.list_nhan_vien.remove(i)
        if c==0:
            print('Không tìm thấy ID')  
    
    def hien_thi(self):
            print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10}'.format(
                'ID','Ten','Tuoi','Que QUan','Chuc Vu','Cham Cong','Luong'))
            for i in self.list_nhan_vien:
                print('{:<4} {:<10} {:<7} {:<10} {:<10} {:<10} {:<10}'.format(
                    i.id,i.ten,i.tuoi,i.queQuan,i.chucVu,i.chamCong,i.luong))