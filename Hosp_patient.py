import sqlite3

details = sqlite3.connect("hospital.db")  # creating a database

details.execute('''   Create Table Patients(
                      PatientID Integer Primary Key Autoincrement,
                      PatientName Text,
                      PatientAddress Text,
                      PatientMobileNumber Integer,
                      PatientMailID Text,
                      PatientPincode Integer
);     ''')

print("Table Created Successfully")