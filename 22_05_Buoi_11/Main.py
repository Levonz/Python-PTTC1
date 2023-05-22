from Tinh_toan.coban import *
from Tinh_toan.Nang_cao.nangcao import *

try:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))

    print(cong(a,b))
    print(tru(a,b))
    print(nhan(a,b))
    print(chia(a,b))
    print('phep nang cao:')
    print(can_bac_hai(a))
    print(binh_phuong(a))
except:
    print("Lỗi")