'''
1.Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py ""Demo
Demo is name of directory.


input:
	  Dirname

output:
	  All files checksum should display

'''
import sys  
import os
import hashlib

def hashfile(path, blocksize = 1024):
	
	afile = open(path,'rb');	
	buf = afile.read();
	print(afile.read())
	afile.close();	
	return hashlib.md5(buf).hexdigest();""		


def DisplayChecksum(path):
	flag = os.path.isabs(path);
	if flag == False:
		path = os.path.abspath(path);	
		if os.path.isdir(path):
			for dirn, surdirns, flnms in os.walk(path):
				for fln in flnms:
					print("FileName: ",fln);
					path = os.path.join(dirn,fln);
					fl_hash = hashfile(path);
					print(fl_hash);
		else:
			print("Invalid input");
	

def main():
	
	print("Appllication Name: ",sys.argv[0]);
	if len(sys.argv) != 2:
		print("Error: invalid number of arguments");
		exit();
		
	try:
		DisplayChecksum(sys.argv[1]);
	
	except Exception as e:
		print("Exception raised ",e);


if __name__ == "__main__":
	main();

