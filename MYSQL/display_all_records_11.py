#Select all records from the "STUDENT" table, and display the result:

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");


if mydb:
	print("connected successfully");

mycursor = mydb.cursor();

mycursor.execute("SELECT * FROM STUDENT");

myresult = mycursor.fetchall(); #this fetchall method fetch all rows and columns data

print("\nDisplaying all records");
for x in myresult:
	print(x);
