from quanLy import *
import connectSql
import mysql.connector

while(True):
    print("|--------------------------------------|")
    print("|----Chuong trinh quan ly nhan vien    |")
    print("|1. Chuc nang Thêm                     |")
    print("|2. Chuc nang Sửa                      |")
    print("|3. Chuc nang Xóa                      |")
    print("|4. Chuc nang Hiển thị                 |")
    print("|5. Chuc nang sap xep theo ten         |")
    print("|0. Thoát                              |")
    print("|--------------------------------------|")
    nhap = int(input('Chọn chức năng bạn muốn theo số: '))
    if nhap==1:
        themNhanVien()
    elif nhap==2:
        id = input("Nhập Id nhân viên muốn sửa: ")
        suaNhanVien(id)
    elif nhap==3:
        id = input("Nhập Id nhân viên muốn xóa: ")
        xoaNhanVien(id)
    elif nhap==4:
        hienThiTatCa()
    elif nhap==5:
        sapxeptheoten()
    elif nhap==0:
        connectSql.getConnection().close()
        print('Thoát')
        break
    else: 
        print('Không có lựa chọn đó!')