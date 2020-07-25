'''
Python MySQL Order By

Use the ORDER BY statement to sort the result in ascending or descending order.

The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.
IN Ascending order showing all recorder one name column
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print(mydb);


mycursor = mydb.cursor();

sql_query = "SELECT * FROM STUDENT ORDER BY std_Name"; # A to Z its ascending

mycursor.execute(sql_query);

myresult = mycursor.fetchall();

for x in myresult:
	print(x);
