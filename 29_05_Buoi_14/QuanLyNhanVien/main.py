from QuanLy import *

while(True):
    print("|--------------------------------------|")
    print("|----Chuong trinh quan ly nhan vien    |")
    print("|1. Chuc nang Thêm                     |")
    print("|2. Chuc nang Sửa                      |")
    print("|3. Chuc nang Xóa                      |")
    print("|4. Chuc nang Hiển thị                 |")
    print("|0. Thoát                              |")
    print("|--------------------------------------|")
    nhap = int(input('Chọn chức năng bạn muốn theo số: '))
    
    QuanLyNhanVien = QuanLyNhanVien()
    if nhap==1:
        QuanLyNhanVien.them()
    elif nhap==2:
        if len(QuanLyNhanVien.list_nhan_vien)!=0:
            t= input('Nhập id học viên muốn sửa: ')
            QuanLyNhanVien.sua(t)
        else:
            print('Hiện không có học viên nào, vui lòng thêm học viên!')
    elif nhap==3:
        if len(QuanLyNhanVien.list_nhan_vien)!=0:
            t= input('Nhập id học viên muốn xóa: ')
            QuanLyNhanVien.xoa(t)
        else:
            print('Hiện không có học viên nào, vui lòng thêm học viên!')
    elif nhap==4:
        QuanLyNhanVien.hien_thi()
    elif nhap==0:
        print('Thoát')
        break
    else: 
        print('Không có lựa chọn đó!')