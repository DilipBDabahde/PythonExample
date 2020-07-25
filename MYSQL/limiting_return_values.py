'''
Limit the Result
You can limit the number of records returned from the query, by using the "LIMIT" statement:

Example: Select the 3 first records in the "STUDENT" table:
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connected to dbms");
	

mycursor = mydb.cursor();

mycursor.execute("SELECT * FROM STUDENT LIMIT 3");	# limit works on rows to return records

result = mycursor.fetchall();	#fetching records as per set value of LIMIT

for x in result:		#after fetched records displaying
	print(x);
