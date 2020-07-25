#in this program we apply where clause to display perticular address


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("connected sucessfully to DBMS");



mycursor = mydb.cursor(); # cursor method is used to deal with row and cols of our tablles

sql_query = "SELECT * FROM STUDENT WHERE std_Address = 'ShektaGaon'";

mycursor.execute(sql_query);

myresult = mycursor.fetchall();

for x in myresult: # here all Where clause values will be displayed
	print(x);

