class PTTC1:
    #Thuộc tính
    def __init__(self,name,age,country,lop):
        self.name = name
        self.age = age
        self.country = country
        self.lop = lop
    #Phương thức
    def an(self):
        print('Phải ăn đầy đủ trước khi tới lớp')
    def hoc(self):
        print(self.name+' Học Python')
    
student1 =PTTC1('Giang',20,'Hà Nội','PTTC1')
print(student1.lop)
student1.an()
student1.hoc()