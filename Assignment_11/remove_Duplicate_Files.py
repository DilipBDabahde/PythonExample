'''
Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory.
Usage : DirectoryDusplicateRemoval.py “Demo”
Demo is name of directory.

Demo/		data					Checksum
|-- a.c		"Hello"					10
|-- ab.c	"World"					11
|-- b.c		"Hello World"			12
|-- mp.c	"Hello"					10
|-- ppa.c	"Hello"					10
`-- x.c		"HelloWorld"			13

above 2 files are duplicate where there checksum is repeated as 10

mp.c ppa.c are duplicate files remove them
'''

import hashlib
import os
from sys import *


def hasher(data):
	return hashlib.md5(data).hexdigest();

def remove_duplicate_files(dirname):
	orglist = [];
	duplist = [];
	
	if not os.path.exists(dirname):
		print(dirname +": directory is not existing");
		exit();
	
	fd1  = open("logfile.text",'w');
	fd1.write("Duplicates files are: \n");
	for fname in os.listdir(dirname):
		if not fname.endswith('~'):
			fullName = os.path.join(dirname, fname);
			#file open and reading operation
			fd = open(fullName, 'rb');
			data = fd.read();
			fd.close();
			
			chksum = hasher(data);
			
			if len(orglist) == 0:
				orglist.append(chksum);
			else:
				if not chksum in orglist:
					orglist.append(chksum);
				else:
					fd1.write(fname+"\n");
					os.remove(fullName);
	fd1.close();

	
	print("Duplicate fiels removed");
	
	

def usage():
	print("Usage: This script is used to find duplicate files.\nBy using checksum it is possible to get easily duplicate files");


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
		remove_duplicate_files(argv[1]);

	except	Exception as e:
		print("Exceptin occured"+ e);
		


if __name__ == "__main__":
	main();

