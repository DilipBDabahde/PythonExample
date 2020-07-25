'''
order by field_name DESC 
this above statment show records in desceing order

for this program we use "select * from tablename order by table_field DESC"
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connected successfully");
else:
	print("not connected to dbms");

mycursor = mydb.cursor();

sql_query = "SELECT * FROM STUDENT order by std_address DESC";

mycursor.execute(sql_query);

myresult = mycursor.fetchall();

for x in myresult:
	print(x);
