#Create primary key on an existing table:

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connection done");
else:
	print("ur not connected with db");
	

mycursor = mydb.cursor();


#If this page is executed with no error, the table "customers" now has a primary key

mycursor.execute("CREATE TABLE STUDENT (std_ID INT AUTO_INCREMENT PRIMARY KEY, std_Name VARCHAR(255), std_Address VARCHAR(255))");



