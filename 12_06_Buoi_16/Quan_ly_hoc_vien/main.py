from Quan_Ly_Hoc_Vien import *
import ConnectSql
import mysql.connector

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
        themHocVien()
    elif nhap==2:
        id = input("Nhập Id học viên muốn sửa: ")
        suaHocVien(id)
    elif nhap==3:
        id = input("Nhập Id học viên muốn xóa: ")
        xoaHocVien(id)
    elif nhap==4:
        getalldata()
    elif nhap==0:
        ConnectSql.getConnection().close()
        print('Thoát')
        break
    else: 
        print('Không có lựa chọn đó!')