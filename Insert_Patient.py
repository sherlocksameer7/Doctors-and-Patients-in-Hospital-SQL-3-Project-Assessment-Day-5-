import sqlite3

details = sqlite3.connect("hospital.db")

get_Patient_Name = input("Enter Patient Name: ")
get_Patient_address = input("Enter Patient Address: ")
get_Patient_Mobile_Number = input("Enter Patient Mobile Number: ")
get_Patient_MailID = input("Enter Patient MailID: ")
get_Patient_Pincode = input("Enter Patient Pincode: ")

details.execute("Insert Into Patients(PatientName, PatientAddress, PatientMobileNumber, PatientMailID, PatientPincode)\
                Values ('"+get_Patient_Name+"','"+get_Patient_address+"',"+get_Patient_Mobile_Number+",\
                '"+get_Patient_MailID+"',"+get_Patient_Pincode+")")

details.commit()
details.close()
print("Inserted Successfully")
