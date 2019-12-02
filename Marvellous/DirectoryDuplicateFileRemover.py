'''
Automation script which accept directory name from user and remove duplicate files from that directory.

for this program first create one director and subdirectory each one contains some filse
	like
				AZ    is a directore
				/\	\
			   /  \	 \
			  /    \  a.c is a file
			  AB   CD\	
			  /\	 /\
			 /  \	/  \
			/    \	a.c b.c
			a.c  x.c
			
			we have AZ,AB,CD directories all have some files a.c is dublicates many times so a.c file will be removed 
			and x.c will be one there		
				
'''
from sys import *
import os
import time
import hashlib



#####################################################################################################		

def hashfile(path,blocksize=1024):
	afile = open(path,'rb');
	hasher = hashlib.md5();
	buf = afile.read(blocksize);
	
	while len(buf)>0:
		hasher.update(buf);
		buf = afile.read(blocksize);
	afile.close();
	
	return hasher.hexdigest();	

#####################################################################################################		

def findDup(path):	# this fun use to find dup files
	
	flag = os.path.isabs(path); # isabs methods chek path is abs or not
	
	if flag == False:	
		path = os.path.abspath(path); # path conversion
		
	exists = os.path.isdir(path); # chk path is dir or not
	
	dups = {}; # empty dict created
	
	if exists: # if cond is True
		for dirName, subDirs, fileList in os.walk(path):
			print("Current folder is: "+dirName);
			for filename in fileList:
				path = os.path.join(dirName,filename);
				file_h = hashfile(path);
				
				if file_h in dups:
					dups[file_h].append(path);
				else:
					dups[file_h]=[path];
		return dups;
	else:
		print("Invalid Path");
		

#####################################################################################################				

def DeleteFiles(dict1):
	results = list(filter(lambda x:len(x)>1, dict1.values()));
	
	icnt = 0;
	
	if len(results)>0:
		for result in results:
			for subresult in result:
				icnt += 1;
				if icnt >= 2:
					os.remove(subresult);
			icnt = 0;
	else:
		print("No Duplicate files found.");

#####################################################################################################		
		
def printResults(dict1):
	
	print(type(dict1));

	results = list(filter(lambda x:len(x) > 1, dict1.values()))

	if len(results) > 0:
		print("Duplicates Found:");
		print("The following files are duplicates");
		for result in results:
			for subresult in result:
				print("\t\t%s"%subresult);
	else:
		print("No Duplicate files found");
	

#####################################################################################################			

def main():	# entry point function

	print("-----Demonstration of duplicate file removals-----")
	
	print("Application name: "+argv[0]);
	
	if (len(argv)!= 2):
		print("Error: invalid number of arguments");
		exit();
	
	if (argv[1]=="-h" or (argv[1]=="-H")):
		print("This script is used to traverse specific directory and delete duplicate files");
		exit();
	
	if (argv[1])== '-u' or (argv[1]=='-U'):
		print("Usage: ApplicationName Absolutepath_of_Directory Extention");
		exit();
	
	try:
		arr = {}; #empty dict created
		startTime = time.time(); # it gives us current time
		arr = findDup(argv[1]); # we pass directoryname to fuction "First call outside main()"
		printResults(arr);
		DeleteFiles(arr);		
		endTime = time.time(); # it gives end time
		
		print("Took %s seconds to evalutes."% (endTime-startTime)); # final we get total time for completing given task
		
	except ValueError:
		print("Error: Invalid datatype of input");
	
	except Exception as E: # generic Exception
		print("Error: Invalid input",E);


#####################################################################################################		

if __name__ == "__main__":
	main();
