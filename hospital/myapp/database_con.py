import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',passwd='')
cursor=a.cursor()
try:
    cursor.execute("create database hdata")
    obj=cursor.execute("show databases")
    print("database created succesfully!!")
except:
    print("no databases found")
for x in cursor:
    print(x)
a.close()