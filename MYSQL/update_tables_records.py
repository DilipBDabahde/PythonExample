'''
You can update existing records in a table by using the "UPDATE" statement:
Example
Overwrite the address column from "Valley 345" to "Canyoun 123":
'''
	
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connected Successfully");
	
mycursor = mydb.cursor();

sql_query = "UPDATE STUDENT SET std_Name = 'Keshav' WHERE std_Address ='Aurangabad'";

mycursor.execute(sql_query);
mydb.commit();

