import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Current-Root-Password", db="TESTDB")


#cursor is used to iterate records

mycursor = mydb.cursor();

mycursor.execute("SHOW TABLES");


for x in mycursor:
	print(x);

