#after creating primary key check table is created or not

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Current-Root-Password", db="TESTDB");

if mydb:
	print("Connection done");


mycursor = mydb.cursor();

mycursor.execute("SHOW TABLES")

print("\nShowing all tables of TESTDB database");

for tbl in mycursor:
	print(tbl);
