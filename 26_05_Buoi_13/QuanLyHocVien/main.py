while(True):
    print("Chọn Chức năng")
    print('1>Thêm học viên')
    print('2>Sửa học viên')
    print('3>Xóa học viên')
    print('4>Hiển thị')
    print('0>Thoát')
    nhap = int(input('Chọn chức năng bạn muốn theo số: '))
    if nhap==1:
        print('thêm')
    elif nhap==2:
        print('Sửa')
    elif nhap==3:
        print('Xóa')
    elif nhap==4:
        print('Hiển thị')
    elif nhap==0:
        print('Thoát')
        break
    else: 
        print('Không có lựa chọn đó!')