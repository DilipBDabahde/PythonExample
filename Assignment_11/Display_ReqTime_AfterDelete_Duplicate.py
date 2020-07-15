'''
Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory. Display execution time required for the
script.
Usage : DirectoryDusplicateRemoval.py “Demo”
Demo is name of directory.


Demo/		data					Checksum
|-- a.c		"Hello"					10
|-- ab.c	"World"					11
|-- b.c		"Hello World"			12
|-- mp.c	"Hello"					10
|-- ppa.c	"Hello"					10
`-- x.c		"HelloWorld"			13

a.c and mp.c and ppa.c these files are same   copy these files into Log.text show req time


'''

import os
import hashlib
from time import *
from sys import *


def hasher(data):

	checksum = hashlib.md5(data).hexdigest();

	return checksum;
	
	
def display_Time_ToRemove_DupFiles(dirname):

	orglist = [];
	duplist = [];
	icnt = 0;
	
	if not os.path.exists(dirname):
		print(dirname+": is not existing");
		exit();
	
	fd1 = open("Log.text",'w');	 	#logfile created
	fd1.write("Duplicate files list\n");
	for fname in os.listdir(dirname):
		fullpath = os.path.join(dirname, fname);
		fd = open(fullpath, 'rb');		#opening file to read data
		data = fd.read();				#red data
		fd.close();						#closed file
		
		checksum = hasher(data);
		
		if len(orglist) == 0:
			orglist.append(checksum);
		else:
			if not checksum in orglist:
				orglist.append(checksum);
			else:
				fd1.write(fname+"\n");
				os.remove(fullpath);
				icnt = icnt + 1;
	
	fd1.write("Total duplicates count is: "+str(icnt));
	fd1.close();
	
	print("Total duplicates count is: ",icnt)
	


def usage():
	print("Usage: This script is used to find duplicate files.\nBy using checksum it is possible to get easily duplicate files\nAfter this operation show req time");


def help():
	print("To use this script input should like:\npytohn3 filename.py Dirname");


def main():
	print("Applicaton name: "+argv[0]);
	
	if argv[1] == '-h' or argv[1]== '-H':
		help();
		exit();
		
	elif argv[1] == 'u' or argv[1] =='U':
		usage();
		exit();
		
	if len(argv) != 2:
		print("insufficient parameters");
		exit();
	
	try:
		st = time();
		display_Time_ToRemove_DupFiles(argv[1]);
		et = time();
		
		print("Time consumed for this task is: ",et - st);

	except	Exception as e:
		print("Exceptin occured"+ e);



if __name__ == "__main__":
	main();



