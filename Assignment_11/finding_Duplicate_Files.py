'''
Design automation script which accept directory name and write names of duplicate files from
that directory into log file named as Log.txt. Log.txt file should be created into current
directory.
Usage : DirectoryDusplicate.py “Demo”
Demo is name of directory.

to solve this problem we have to compare file file checksum 
each file has only one checksum but there should be same hasher

Demo
   |__Files__ a.c b.c ab.c ppa.c

   a.c  "Hello"
   b.c	"World"
   ab.c "HelloWorld"
   ppa.c "Hello"			This file contains same data ppa.c is duplicate

'''

import hashlib
from sys import *
import os


def hasher(data):
	
	return hashlib.md5(data).hexdigest();	


def finding_duplicate(dirname):

	dict1 = [] ; #empty dict is created
	dup = []
	
	if not os.path.exists(dirname):
		print(dirname +": directory is not existing");
	
	for fname in os.listdir(dirname):
		if fname.endswith('~'):
			fn = os.path.join(dirname, fname)
			os.remove(fn)	#deleting files which ends with '~'
		else:
			fnaav = os.path.join(dirname, fname)
			fd = open(fnaav, 'rb');
			data = fd.read(); #file data is copyied successfully
			fd.close();		# reading operation is done close now openedfile
			
			chksum = hasher(data);
			
			if len(dict1) == 0:
				dict1.append(chksum);
			else:
				if not chksum in dict1:
					dict1.append(chksum);
				else:
					dup.append(fname);
			chksum= 0;
					
					
	#creating log file
	fd = 0;
	icnt = 0;
	
	fd = open("Log.text", 'w');
	fd.write("Duplicate files are:\n");
	for i in dup:
		icnt = icnt + 1
		fd.write(i+'\n');
	fd.write("Total duplates files are: "+str(icnt))
	fd.close();
	

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
		finding_duplicate(argv[1]);
		print("Operation DONE")
	except	Exception as e:
		print("Exceptin occured"+ e);
		


if __name__ == '__main__':
	main()
