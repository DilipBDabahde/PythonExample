#accepting size of records from user and then after accept values for all records


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

#records_size  = int(input("Enter size of records: "));

print("Showing all tables");

mycursor = mydb.cursor();

size = int(input("Enter records size: "));

i = 1;
Name = None;
Adds = None;

while i <= size:
	
	sql = "INSERT INTO STUDENT (std_Name, std_Address) VALUES (%s, %s)"
	print("Rocord Num: ",i,": ");
	Name = input("Enter name: ");
	Adds = input("Enter address: ");
	val = (Name, Adds);
	mycursor.execute(sql, val)
	mydb.commit()
	i = i + 1;


