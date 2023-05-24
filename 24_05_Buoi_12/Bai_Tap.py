#Tạo ra một class, định nghĩa class đó
#Tạo ra 10 đối tượng trong class
#In ra danh sách tên 10 đối tương trong class

class product():
    def __init__(self,id,name,price,isAvailable):
        self.id = id
        self.name = name
        self.price = price
        self.isAvailable = isAvailable

Product = []

Product.append(product('01','Bánh',200000,True))  
Product.append(product('02','Quần',300000,True))
Product.append(product('03','Áo',150000,True))
Product.append(product('04','Giầy',700000,True))
Product.append(product('05','Mũ',40000,True))
Product.append(product('06','Bóng',135000,True))
Product.append(product('07','Súng',1000000,False))
Product.append(product('08','Gậy',99000,True))
Product.append(product('09','Xe',400000,True))
Product.append(product('10','Khăn',60000,True))

for i in Product:
    print(i.name)


        