class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def an(self):
        print('phải ăn')
    def ngu(self):
        print('phải ngủ')
    def hoc(self):
        print("Đi học 2")
class BKCAD():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def hoc(self):
        print('Đi học 1')
    def thi(self):
        print('Phải thi')

#Tính Kế thừa
class PTTC1(BKCAD,Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def giaoluu(self):
        print('Giao Lưu PTTC1')
class PTTC2(BKCAD):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def giaoluu(self):
        print('Giao Lưu PTTC2')   
        
class PTTC1_offline(PTTC1):        
    def __init__(self,name,age):
        self.name = name
        self.age = age
  
#Tính Đa hình
def da_hinh(student):
    student.giaoluu()      
    
student1 = PTTC1('Quang',22)

student2 = PTTC1_offline('Hoàng',23)

student3 = PTTC2('Tiến',32)
da_hinh(student1)
da_hinh(student3)