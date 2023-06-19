import ConnectSql

ketnoi = ConnectSql.getConnection()
dulieu = ketnoi.cursor()

def getalldata():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    print('{:<4} {:<15} {:<7} {:<10} {:<10} {:<13} {:<10}'.format(
            'Id','Name','Age','Class','English','Information','Xếp loại'))
    for i in ketqua:
        diemTB = (i[-1] + i[-2])/2
        if diemTB>5:
            hocLuc = 'Giỏi'
        else:
            hocLuc = 'Khá'
        print('{:<4} {:<15} {:<7} {:<10} {:<10} {:<13} {:<10}'.format(
            i[0],i[1],i[2],i[3],i[4],i[5],hocLuc))
        
       
def getalldata2():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()
        
def getalldatatest():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    print(ketqua)
        
        
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
        id =input('Id: ')
        name = input('Name: ')
        age = int(input('Age: '))
        country = input('Country: ')
        english = float(input('English: '))
        information = float(input('Information: '))
        dulieu.execute("INSERT INTO quan_ly_hoc_vien.hocvien(Id,`Name`,Age,Country,English,Information) VALUES({},'{}',{},'{}',{},{})"
                       .format(id,name,age,country,english,information))
        ketnoi.commit()
    
def suaHocVien(id):
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    exist = False
    for i in ketqua:
        if i[0] == id:
            exist = True
            break
    if exist == True:
        name = input('Name: ')
        age = int(input('Age: '))
        country = input('Country: ')
        english = float(input('English: '))
        information = float(input('Information: '))
        sql ="UPDATE quan_ly_hoc_vien.hocvien SET `Name` = %s,Age = %s,Country = %s,English = %s,Information = %s WHERE Id = %s"
        dulieu.execute(sql,(name,age,country,english,information,id))
        ketnoi.commit()
    else:
        print('Id không tồn tại!')
    
def xoaHocVien(id):
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchall()
    exist = False
    for i in ketqua:
        if i[0] == id:
            exist = True
            break
    if exist == True:
        sql = "DELETE FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(id)
        dulieu.execute(sql)
        ketnoi.commit()
    else:
        print('Id không tồn tại!')
    
#getalldatatest()