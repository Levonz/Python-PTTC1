from Quan_Ly_Hoc_Vien import *

while(True):
    print("|--------------------------------------|")
    print("|----Chuong trinh quan ly hoc vien     |")
    print("|1. Chuc nang Thêm                     |")
    print("|2. Chuc nang Sửa                      |")
    print("|3. Chuc nang Xóa                      |")
    print("|4. Chuc nang Hiển thị                 |")
    print("|0. Thoát                              |")
    print("|--------------------------------------|")
    nhap = int(input('Chọn chức năng bạn muốn theo số: '))
    if nhap==1:
        QuanLyHocVien.Them_Hoc_Vien()
    elif nhap==2:
        if len(QuanLyHocVien.list_hoc_vien)!=0:
            t= int(input('Nhập id học viên muốn sửa: '))
            QuanLyHocVien.Sua_Thong_Tin_Hoc_Vien(t)
        else:
            print('Hiện không có học viên nào, vui lòng thêm học viên!')
    elif nhap==3:
        if len(QuanLyHocVien.list_hoc_vien)!=0:
            t= int(input('Nhập id học viên muốn xóa: '))
            QuanLyHocVien.Xoa_Hoc_Vien(t)
        else:
            print('Hiện không có học viên nào, vui lòng thêm học viên!')
    elif nhap==4:
        QuanLyHocVien.Hien_Thi_Hoc_Vien()
    elif nhap==0:
        print('Thoát')
        break
    else: 
        print('Không có lựa chọn đó!')