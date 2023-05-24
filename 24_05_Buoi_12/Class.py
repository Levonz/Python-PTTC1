class PTTC1():
    #Thuộc tính
    name = 'abc'
    age = 0
    country = 'HN'
    #Phương thức
    def hoc(self):
        print('Phải học Python')
    def thi(self):
        print('Phải thi Python')
     
student1 = PTTC1()
student1.name = 'Nguyen Van A'
student1.age = '20'
student1.country = 'Ha Noi'

student2 = PTTC1()
student2.name = 'Nguyen Van B'
student2.age = '21'
student2.country = 'Ha Noi'

student3 = PTTC1()
student3.name = 'Nguyen Van C'
student3.age = '20'
student3.country = 'Bac Ninh'

print(student1.name)
print(student2.name)
print(student3.name)

student1.hoc()