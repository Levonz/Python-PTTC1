def chia(a,b):
    return a/b

def tinh(a,b):
    return a+b+2*b+2*a
#Viết 1 hàm nhập vào 1 số từ bàn phím, tính căn bậc 2 của số đó
#Dùng Try- Except để xử lý trong trường hợp người dùng đó không nhập số mà nhập chữ
def can_bac_2():
    try:
        a= int(input("Nhập a: "))
        print('Can bac 2:',a**1/2)
    except:
        print('Yêu cầu nhập chữ số')
    return()

can_bac_2()