'''
Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement:

'''

import mysql.connector 

mydb = mysql.connector.connect(host="localhost", user="root", db="TESTDB", password="Current-Root-Password");


if mydb:
	print("Connected Successfully")
	

mycursor = mydb.cursor();

sql_query = "DELETE FROM STUDENT WHERE std_Address = 'ShektaGaon'";

mycursor.execute(sql_query); 


'''
Important!: Notice the statement: mydb.commit(). It is required to make the changes,
otherwise no changes are made to the table.	
'''
mydb.commit();

print(mycursor.rowcount, "records Deleted");

	
	
