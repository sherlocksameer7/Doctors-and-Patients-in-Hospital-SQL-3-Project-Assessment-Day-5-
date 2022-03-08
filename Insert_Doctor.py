import sqlite3

connection = sqlite3.connect("hospital.db")

get_doctor_name = input("Enter a Doctor's Name: ")
get_doctor_qualification = input("Enter a Doctor's Qualification: ")
get_doctor_address = input("Enter a Doctor's Address: ")
get_doctor_mob_Num = input("Enter a Doctor's Mobile Number: ")
get_doctor_mailID = input("Enter a Doctor's Mail ID: ")

connection.execute("Insert Into Doctor(Doctors_Name, Doctors_Qualification, Doctors_Address, Doctors_Mob_Num, Doctors_Mail_ID) \
                Values ('"+get_doctor_name+"','"+get_doctor_qualification+"','"+get_doctor_address+"',\
                "+get_doctor_mob_Num+",'"+get_doctor_mailID+"')")

connection.commit()
connection.close()

print("Inserted Successfully")