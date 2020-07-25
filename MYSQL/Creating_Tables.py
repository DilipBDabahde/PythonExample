#creating table

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "root", password = "Current-Root-Password", db="TESTDB");

print("Connection successfull: \n", mydb);

#To create a table in MySQL, use the "CREATE TABLE" statement.


mycursor = mydb.cursor();


mycursor.execute("CREATE TABLE 	curstomers (name VARCHAR(255), 	address VARCHAR(255))");

#
#If this page is executed with no error, you have successfully created a table named "customers".
