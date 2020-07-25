'''
we can delete an existing table by using the "DROP TABLE" statement:

Example
Delete the table "STUDENT":
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connected sucessfully");


mycursor = mydb.cursor();

sql_query = "DROP TABLE IF EXISTS STUDENT";
mycursor.execute(sql_query);

print("drop table sucessfully");
#after dropped table & if we check then there  is error pron like below
#ERROR 1146 (42S02): Table 'TESTDB.STUDENT' doesn't exist
#mysql.connector.errors.ProgrammingError: 1051 (42S02): Unknown table 'TESTDB.STUDENT'



