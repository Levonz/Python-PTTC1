import mysql.connector

def getConnection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'giang123',
        database = 'quan_ly_hoc_vien',
    )
    return connection