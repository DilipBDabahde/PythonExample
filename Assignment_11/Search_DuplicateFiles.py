'''
2.Design automation script which accept directory name and write names of duplicate files from that directory into
log file named as Log.txt. Log.txt file should be created into current directory.

Usage : DirectoryDusplicate.py Demo
Demo is name of directory.


in this script we have to take directory name from user and write duplicate files name into Log.txt file create Log.txt fil
run time

dirname:				FileName: 
		Demo		     		 Log.txt	
		|A.c			         |A.c 		is duplicate file in Demo directory
		|B.c								we have to create Log.txt at run time
		|A.c
		|K.java
		|l.cpp					
'''

import time
import sys
import os
import hashlib

def read_fileobjbin(fobj, chunk_size=1024):
    
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def Finding_Dup_Files(paths, hash=hashlib.md5):
    dict1 = {}
    icnt = 0;
    fl = open("Log.txt",'w');   
    fl.close;
    
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                f_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in read_fileobjbin(open(f_path, 'rb')):
                    hashobj.update(chunk)
                f_id = (hashobj.digest(), os.path.getsize(f_path)) # fileid is like node id
                duplicate = dict1.get(f_id, None)
                if duplicate:
                    print "Duplicate files: %s ---->>  %s" % (f_path, duplicate)
                    fl = open("Log.txt",'a');
                    fl.write(f_path);
                    fl.write("\n");
                    fl.close();
                    print("-------------------------------------------------");
                    icnt = icnt + 1;
                else:
                    dict1[f_id] = f_path
	
	if icnt != 0:
		fl = open("Log.txt",'a');
		fl.write("Total duplicates files are: ");
		fl.write("%s" % icnt);
		fl.write("\n");
		fl.close();
	print("Total duplicate file ",icnt);


def main():

	print("Application Name: ",sys.argv[0]);
	if len(sys.argv) != 2:
		print("Invalid input:")
		exit();
		
	st = time.time();
	Finding_Dup_Files(sys.argv);
	et = time.time();
	print("Req time is: ",et-st);

if __name__ =="__main__":
	main();
	
	
