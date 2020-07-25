#If you are only interested in one row, you can use the fetchone() method.

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");


if mydb:
	print("Connected to DBMS successfully");



mycursor = mydb.cursor(); #cursor method is used to deal with row and cols of our db

mycursor.execute("SELECT * FROM STUDENT");

myresult = mycursor.fetchone();

print("Only one record fetched: ", myresult); #first record is fetched successfully
