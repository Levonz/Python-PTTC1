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

getdatabyid(3)
ketnoi.close()