#inserting multiple records
import mysql.connector

mydb = mysql.connector.connect(host="localhost", db="TESTDB", user="root", password="Current-Root-Password");

if mydb:
	print("connected sucessfully");


#now we have to accept student name and his address from user and add it to STUDENT table of TESTDB

records_size = int( input("Enter how many entries you want: "));

mycursor = mydb.cursor(); # need to use mycursor to store values

i = 1;
name = None;
address = None;
	
while i <= records_size:
	# in this loop we access values from user and store them into database tablles 
	name = input("Enter Student name: ");
	address = input("Enter Student address: ");
	
	var = "INSERT INTO STUDENT (std_Name, std_Address) VALUES (%s, %s)"
	val = (name, address);
	
	mycursor.execute(var, val);
	mydb.commit();
	i += 1;


print(records_size, "records inserted");





