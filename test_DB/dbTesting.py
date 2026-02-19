import sqlite3

def test_sqlite3():
   liteConnection =  sqlite3.connect(r"C:\Users\Nikitha\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")
   script = liteConnection.cursor()
   script.execute("SELECT a.Title, a.AlbumId  from Album a")
#    print(script.fetchmany(10))
#    print(script.fetchone().count)
   rows =script.fetchall()
   print(len(rows))
#    print(script.rowcount)
#    print(script.fetchall())
    
    # result = script.fetchall



# pip install mysql-connector-python

# import mysql.connector

# def test_mysql():
#    mysqlConnector =  mysql.connect(host="url",database="",username="",password="")
#    script = mysqlConnector.cursor()
#    script.execute("SELECT a.Title, a.AlbumId  from Album a")
# #    print(script.fetchmany(10))
# #    print(script.fetchone().count)
#    rows =script.fetchall()
#    print(len(rows))



# # pip install pyscopyg2-binary
# import pyscopyg2

# def test_mysql():
#    postGressConnector =  pyscopyg2.connect(host="url",database="",username="",password="",port="")
#    script = postGressConnector.cursor()
#    script.execute("SELECT a.Title, a.AlbumId  from Album a")
# #    print(script.fetchmany(10))
# #    print(script.fetchone().count)
#    rows =script.fetchall()
#    print(len(rows))


