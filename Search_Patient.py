import sqlite3

connection = sqlite3.connect("hospital.db")

get_patient_ID = input("Enter a Patient ID to be Searched? ")

result = connection.execute("Select * From Patients Where PatientID=" +get_patient_ID)

for i in result:
    print("Patient ID", i[0])
    print("Patient Name", i[1])
    print("Patient Address", i[2])
    print("Patient Mobile Number", i[3])
    print("Patient MailID", i[4])
    print("Patient Pincode", i[5])
