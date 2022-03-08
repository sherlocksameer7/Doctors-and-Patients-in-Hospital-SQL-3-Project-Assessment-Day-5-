import sqlite3

connection = sqlite3.connect("hospital.db")

result = connection.execute("Select * From Doctor")

for i in result:
    print("Doctors ID", i[0])
    print("Doctors Name", i[1])
    print("Doctors Qualification", i[2])
    print("Doctors Address", i[3])
    print("Doctors Mobile Number", i[4])
    print("Doctors Mail ID", i[5])
