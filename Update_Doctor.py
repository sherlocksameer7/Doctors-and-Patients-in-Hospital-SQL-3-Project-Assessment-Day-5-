import sqlite3

connection = sqlite3.connect("hospital.db")

get_doctors_mob_num = input("Enter a Doctor's Mobile Number to be Updated?  ")

get_doctor_name = input("Enter a New Doctor's Name: ")
get_doctor_qualification = input("Enter a  New Doctor's Qualification: ")
get_doctor_address = input("Enter a New Doctor's Address: ")
get_doctor_mailID = input("Enter a New Doctor's Mail ID: ")

connection.execute("Update Doctor Set Doctors_Name= '"+get_doctor_name+"', Doctors_Qualification= '"+get_doctor_qualification+"',\
 Doctors_Address= '"+get_doctor_address+"', Doctors_Mail_ID= '"+get_doctor_mailID+"'")

result = connection.execute("Select * From Doctor")

for i in result:
    print("Doctors ID", i[0])
    print("Doctors Name", i[1])
    print("Doctors Qualification", i[2])
    print("Doctors Address", i[3])
    print("Doctors Mobile Number", i[4])
    print("Doctors Mail ID", i[5])
