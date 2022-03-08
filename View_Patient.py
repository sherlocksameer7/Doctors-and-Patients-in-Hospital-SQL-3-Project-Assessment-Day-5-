import sqlite3

connection = sqlite3.connect("hospital.db")

result = connection.execute("Select * From Patients")

for i in result:
    print("Patient ID", i[0])
    print("Patient Name", i[1])
    print("Patient Address", i[2])
    print("Patient Mobile Number", i[3])
    print("Patient MailID", i[4])
    print("Patient Pincode", i[5])
