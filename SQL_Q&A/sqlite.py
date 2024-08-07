import sqlite3

#connect tp sqlite3
connection=sqlite3.connect('student.db')


#create a cursor object to insert
cursor=connection.cursor()

table_info="""
CREATE TABLE studen(NAME varchar(20),Class varchar(25)
,section varchar(25),MARKS int)
"""


cursor.execute(table_info)

cursor.execute('''INSERT INTO student VALUES('Rahul','10th','A',90)''')
cursor.execute('''INSERT INTO student VALUES('John','10th','B',50)''')
cursor.execute('''INSERT INTO student VALUES('Mukesh','9th','A',90)''')
cursor.execute('''INSERT INTO student VALUES('Jacob','8th','C',80)''')
cursor.execute('''INSERT INTO student VALUES('Dipesh','10th','A',90)''')

print("Data inserted successfully")
data=cursor.execute("SELECT * FROM student")

for row in data:
    print(row)
connection.commit()
connection.close()