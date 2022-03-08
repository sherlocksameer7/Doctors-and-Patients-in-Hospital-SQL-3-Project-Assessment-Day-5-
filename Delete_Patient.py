import sqlite3

connection = sqlite3.connect("hospital.db")

get_patient_ID = input("Enter a Patient_ID to be Deleted?  ")

connection.execute("Delete from Patients Where PatientID=" +get_patient_ID)

connection.commit()

print("Deleted Successfully")

result = connection.execute("Select * From Patients")

for i in result:
    print("Patient ID", i[0])
    print("Patient Name", i[1])
    print("Patient Address", i[2])
    print("Patient Mobile Number", i[3])
    print("Patient MailID", i[4])
    print("Patient Pincode", i[5])
