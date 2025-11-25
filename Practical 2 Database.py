#Palak Jaiswal
#F088
#Step 1 : Database connection
import sqlite3
connection = sqlite3.connect ("MVLU_CS_Department.db")
print(connection.total_changes)

#Step 2 : Adding data in database(MVLU_CS_Department)
cursor = connection.cursor()
#cursor = connection.execute("Create table Students1 (Roll_no int, Name varchar(50), Class varchar(50), Course varchar(50))")
connection.commit()
print("Students1 table created.")

#Step 3 : Inserting value in database
cursor.execute("insert into Students1 values(88, 'Palak', 'FYCS', 'Computer Science')")
cursor.execute("insert into Students1 values(69, 'Pranay', 'SYIT', 'Information Technology')")
cursor.execute("insert into Students1 values(75, 'Abhishek', 'FYBT', 'Biotechnology')")
cursor.execute("insert into Students1 values(90, 'Sakshi', 'FYCS', 'Computer Science')")
connection.commit()
print("Value inserted Successfully!")

#Step4 : Update value in database
from sqlite3 import *
connection = connect('MVLU_CS_Department.db')
cur = connection.cursor()
connection.execute ("update Students1 set Roll_no = 77 where Name = 'Pranay'")
connection.commit()
print(" Total No.of row updated ")
connection.close

#Step5 : Select value in database
from sqlite3 import *
connection = connect('MVLU_CS_Department.db')
cur = connection.cursor()
data = connection.execute ("select * from Students1")
print (type(data))
for record in data:
    print("Name :", record[0])
    print("Roll_no : ", record[1])
    print(" Class : ", record[2])
    print(" Course  : ", record[3])
    print("##"*25)
connection.close

#Step6 : Ececute Table
connection = connect('MVLU_CS_Department.db')
cur = connection.cursor()
val = [(88, "Palak", "FYCS", "Computer Science"), (69, "Pranay", "SYIT", "Information Technology"), (75, "Abhishek", "FYBT", "Biotechnology"), (90, "Sakshi", "FYCS", "Computer Science")]
cur.executemany(" insert into Students1 values(?, ?, ?, ?)", val)
print ("Multi data")
connection.commit()
connection.close()


