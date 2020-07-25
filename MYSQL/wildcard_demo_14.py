'''
Wildcard Characters
You can also select the records that starts, includes, or ends with a given letter or phrase/str
Use the %  to represent wildcard characters:
'''
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");

if mydb:
	print("Connection done");


mycursor = mydb.cursor();
													#LIKE next %Gaon%	<---> this should be in single or double quots
sql_query = "SELECT * FROM STUDENT WHERE std_Address LIKE '%gaon%'" # Gaon is connected to end of vill

mycursor.execute(sql_query);

myresult = mycursor.fetchall();

for x in myresult:
	print(x);


