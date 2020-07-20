
import pyodbc
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=G:\programming\БД\Access_sql\Access_sql.mdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
'''for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)'''
crsr.execute("select * from classes")
row=crsr.fetchall()
print(row)
crsr.execute("SELECT SUM(price) AS SUM, AVG(speed) as SPEED_AVERAGE FROM laptop;")
new_row=crsr.fetchall()
print(new_row)
string = "CREATE TABLE Customers(ID varchar(10)NOT NULL PRimary key, Custom_name varchar(25)NOT NULL, Custom_address varchar(25) NULL,Custom_city varchar(25) NULL,Custom_Country varchar(25) NULL,ArcDate varchar(25) NOT NULL)"
crsr.execute(string)
crsr.execute("ALTER TABLE pc ADD Phone varchar(20)")
crsr.execute("ALTER TABLE pc DROP COLUMN Phone")
crsr.execute("DROP TABLE Customers")
crsr.execute("INSERT INTO product(maker,model) VALUES ('F',1500)")
cnxn.commit()
