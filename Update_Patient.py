import sqlite3

connection = sqlite3.connect("hospital.db")

get_patient_ID = input("Enter a Patient ID to be Updated? ")

get_Patient_Name = input("Enter New Patient Name: ")
get_Patient_Address = input("Enter New Patient Address: ")
get_Patient_Mobile_Number = input("Enter New Mobile for Patients: ")
get_Patient_MailID = input("Enter New MailID for Patients: ")
get_Patient_Pincode = input("Enter New Pincode of Patients: ")

connection.execute("Update Patients \
Set PatientName= '"+get_Patient_Name+"', PatientAddress= '"+get_Patient_Address+"',\
 PatientMobileNumber= "+get_Patient_Mobile_Number+", PatientMailID= '"+get_Patient_MailID+"',\
  PatientPincode= "+get_Patient_Pincode+"")

result = connection.execute("Select * From Patients")

for i in result:
    print("Patient ID", i[0])
    print("Patient Name", i[1])
    print("Patient Address", i[2])
    print("Patient Mobile Number", i[3])
    print("Patient MailID", i[4])
    print("Patient Pincode", i[5])
