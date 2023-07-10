import ConnectSQL
import mysql.connector

ketnoi = ConnectSQL.getConnection()
dulieu = ketnoi.cursor()

print (ketnoi.is_connected())