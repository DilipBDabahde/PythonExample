'''
Selecting Columns :-To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s)
'''

import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connect Successfully");


mycursor = mydb.cursor(); #cursor() method is used to deal with row and col of tables and tables too

mycursor.execute("SELECT std_Name from STUDENT"); #ONLY SELECTED std_Name colums from STUDENT Table

myresult = mycursor.fetchall();

for x in myresult: #displaying only student names
	print(x);
