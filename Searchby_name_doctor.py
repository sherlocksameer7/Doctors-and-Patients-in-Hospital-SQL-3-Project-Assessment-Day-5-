import sqlite3

connection = sqlite3.connect("hospital.db")

get_Doctor_Name = input("Enter a Doctor's Name to be Searched? ")

result = connection.execute("Select * From Doctor Where Doctors_Name= '"+get_Doctor_Name+"'")  # mandatory to check ***

for i in result:
    print("Doctors ID", i[0])
    print("Doctors Name", i[1])
    print("Doctors Qualification", i[2])
    print("Doctors Address", i[3])
    print("Doctors Mobile Number", i[4])
    print("Doctors Mail ID", i[5])