import ConnectSql

ketnoi = ConnectSql.getConnection()
dulieu = ketnoi.cursor()

def getalldata():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
        
       
def getalldata2():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()
        
        
def getdatabyid(t):
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(t))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
#SELCT * FROM quan_ly_hoc_vien.hocvien
def getdatabyid2(id):
    sql = "SELECT * FROM quan_ly_hoc_vien.hocvien WHERE Id = %s"
    dulieu.execute(sql,(id,))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def themHocVien():
    t = int(input('Nhập số lượng học viên muốn thêm: '))
    for i in range(0,t):
        name = input('Name: ')
        age = int(input('Age: '))
        country = input('Country: ')
        english = float(input('English: '))
        information = float(input('Information: '))
        dulieu.execute("INSERT INTO quan_ly_hoc_vien.hocvien(`Name`,Age,Country,English,Information) VALUES('{}',{},'{}',{},{})"
                       .format(name,age,country,english,information))
        ketnoi.commit()
    
def suaHocVien(id):
    name = input('Name: ')
    age = int(input('Age: '))
    country = input('Country: ')
    english = float(input('English: '))
    information = float(input('Information: '))
    sql ="UPDATE quan_ly_hoc_vien.hocvien SET `Name` = %s,Age = %s,Country = %s,English = %s,Information = %s WHERE Id = %s"
    dulieu.execute(sql,(name,age,country,english,information,id))
    ketnoi.commit()
    
def xoaHocVien(id):
    sql = "DELETE FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(id)
    dulieu.execute(sql)
    ketnoi.commit()
