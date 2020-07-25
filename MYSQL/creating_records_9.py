#Insert a record in the "STUDENT" table:

import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="root", db="TESTDB", password= "Current-Root-Password");

if mydb:
	print("Connect Successfully");


mycursor = mydb.cursor();

#now using mycursor execute the query



variables = "INSERT INTO STUDENT (std_Name, std_Address) VALUES (%s, %s)"
values = ("Vidya","Paithan");

mycursor.execute(variables, values);

mydb.commit();

print(mycursor.rowcount	, "record inserted");

















