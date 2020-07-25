import mysql.connector
import pymysql

db =  pymysql.connect("localhost","root","Current-Root-Password","TESTDB" );

cursor = db.cursor();

#select SQL query using execute() method

cursor.execute("SELECT VERSION()");

#just fetch single row using fetchone() method

data = cursor.fetchone();
print("Data version: %s"%data);

#desconnect from server

db.close();
