import sqlite3

details = sqlite3.connect("hospital.db")

details.execute('''   Create Table Doctor(
                      Doctors_ID Integer Primary Key Autoincrement,
                      Doctors_Name Text,
                      Doctors_Qualification Text,
                      Doctors_Address Text,
                      Doctors_Mob_Num Integer,
                      Doctors_Mail_ID Text
);     ''')

print("Table created Successfully")