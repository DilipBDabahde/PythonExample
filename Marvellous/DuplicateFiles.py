'''
Automation script which accept directory name from user and display all names of duplicate files from that directory.
'''


from sys import *
import os
import hashlib


def hashfile(path, blocksize=1024):
	fd = open(path,'rb'); # read mode with binary
	hasher = hashlib.md5();
	buf = fd.read(blocksize);
	
	while len(buf) > 0:
		hasher.update(buf);
		buf= fd.read(blocksize);
		
	fd.close();
	
	return hasher.hexdigest();

def FindDuplicate(path):
	flag = os.path.isabs(path);
	
	if flag == False:
		path = os.path.abspath(path);
	exists = os.path.isdir(path);
	
	dups = {}; #empty dictionary
	
	if exists:
		for dirName,subDirs,files in os.walk(path):
			for filename in files:
				path = os.path.join(dirName,filename);
				f_hash = hashfile(path);
				if f_hash in dups:
					dups[f_hash].append(path);
				else:
					dups[f_hash]=[path];
		return dups;
	else:
		print("Invalid path");

def PrintDuplicate(dict1):
	results = list(filter(lambda X: len(X) > 1, dict1.values()))
	
	if len(results)>0:
		print("Duplicates Found:");
		print("The following files are found");
		
		icnt = 0;
		
		for result in results:
			for subresult in result:
				icnt += 1;
				if icnt >= 2:
					print('\t\t%s' %subresult);
				else:
					print("No duplicate files found");

def main():
	print("Demonstration of finding duplicates files");
	
	print("Application name: ",argv[0]);
	
	if len(argv) != 2:
		print("Error : invalid number of arguments");
		exit();
	
	if argv[1]== '-h' or argv[1]== '-H':
		print("This script is used to traverse specific directory and display sizes of files");
		exit();
	
	if argv[1]=='-u' or argv[1]=='-U':
		print("Usage : ApplicationName AbsolutePath of Directory Extention");
		exit();
	
	try:
		arr = {};
		arr = FindDuplicate(argv[1]);
		PrintDuplicate(arr);
		
	except ValueError:
		print("Error: Invalid datatype of input");
		
if __name__ == "__main__":
	main()
