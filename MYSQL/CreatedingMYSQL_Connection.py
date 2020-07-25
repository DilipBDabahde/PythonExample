#creating connection

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = 'root', password = "Current-Root-Password");

print(mydb); #successfully connected


