import connectSql

ketnoi = connectSql.getConnection()
dulieu = ketnoi.cursor()

def getalldata():
    sql ='SELECT * FROM quan_ly_nhan_vien.nhanvien'
    dulieu.execute(sql)
    ketqua = dulieu.fetchall()
    return(ketqua)

def tinhLuong():
    ketqua = getalldata()
    newList = []
    for i in ketqua:
        luong = i[-1]*300000
        if i[-2]=='TP':
            luong = luong*1.6
        elif i[-2]=='GD':
            luong = luong*2
        i=list(i)
        i.append(luong)
        i=tuple(i)
        newList.append(i)
    return(newList)

def sinhId():
    ketqua=tinhLuong()
    TP = 1
    GD = 1
    NV = 1
    newList=[]
    for i in ketqua:
        id = i[0]
        if i[-3] == 'TP':
            i = list(i)
            newId=i[-3]+str(TP)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            TP+=1
        elif i[-3] == 'NV':
            i = list(i)
            newId=i[-3]+str(NV)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            NV+=1
        elif i[-3] == 'GD':
            i = list(i)
            newId=i[-3]+str(GD)
            i.append(newId)
            i = tuple(i)
            newList.append(i)
            GD+=1
    return(newList)

def hienThiTatCa():
    ketqua = sinhId()
    
    print('{:<4} {:<15} {:<7} {:<10} {:<10} {:<13} {:<10}'.format(
            'ID','Name','Age','Country','Chuc Vu','So ngay lam','Luong'))
    for i in ketqua:
        print('{:<4} {:<15} {:<7} {:<10} {:<10} {:<13} {:<10}đ'.format(
            i[-1],i[1],i[2],i[3],i[4],i[5],str(i[6])+'đ'))
        
def themNhanVien():
    t = int(input('Nhập số lượng nhân viên muốn thêm: '))
    for i in range(0,t):
        print('Nhan vien {}'.format(i+1))
        name = input('Name: ')
        age = int(input('Age: '))
        country = input('Country: ')
        Chucvu = input('Chuc vu: ')
        while(Chucvu != 'NV' and 'TP' and 'GD'):
            print('Khong co chuc vu do!')
            Chucvu = input('Chuc vu: ')
        Songaylam = int(input('So ngay lam: '))
        dulieu.execute("INSERT INTO quan_ly_nhan_vien.nhanvien(`Name`,Age,Country,Chucvu,Songaylam) VALUES('{}','{}','{}','{}',{})"
                       .format(name,age,country,Chucvu,Songaylam))
        ketnoi.commit()
    
def suaNhanVien(newId):
    ketqua = sinhId()
    exist = False
    for i in ketqua:
        if i[-1] == newId:
            id = i[0]
            exist = True
            break
    if exist == True:
        name = input('Name: ')
        age = int(input('Age: '))
        country = input('Country: ')
        Chucvu = input('Chuc vu: ')
        Songaylam = input('So ngay lam: ')
        sql ="UPDATE quan_ly_nhan_vien.nhanvien SET `Name` = %s,Age = %s,Country = %s,Chucvu = %s,Songaylam = %s WHERE Id = %s"
        dulieu.execute(sql,(name,age,country,Chucvu,Songaylam,id))
        ketnoi.commit()
    else:
        print('Id không tồn tại!')
    
def xoaNhanVien(newId):
    ketqua=sinhId()
    exist = False
    for i in ketqua:
        if i[-1] == newId:
            exist = True
            id = i[0]
            break
    if exist == True:
        sql = "DELETE FROM quan_ly_nhan_vien.nhanvien WHERE Id = '{}'".format(id)
        dulieu.execute(sql)
        ketnoi.commit()
    else:
        print('Id không tồn tại!')
        
def sapxeptheoten():
    ketqua=sinhId()
    listName = []
    for i in ketqua:
        listName.append(i[1].split()[-1])
        
    listName.sort()
    for j in listName:
        for i in ketqua:
            if i[1].split()[-1] == j:
                print('{:<4} {:<15} {:<7} {:<10} {:<10} {:<13} {:<10}'.format(
                    i[-1],i[1],i[2],i[3],i[4],i[5],str(i[6])+'đ'))

#sapxeptheoten()
sinhId()