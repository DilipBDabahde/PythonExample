from sys import *;
import os


def DirectoryWatcher(path):
	
	flag = os.path.isabs(path);
	
	if flag == False:
		path= os.path.abspath(path);
	
	exists = os.path.isdir(path);
	
	if exists:
		for fldname, subfld, flname in os.walk(path):
			print("Current folder is: "+fldname);
			for subf in subfld:
				print("Sub folder of:"+fldname+" is: ",	subf);
			
			for fl in flname:
				print("File inside"+ fldname+" is:"+fl);
			print(" ");
	else:
		print("invalid path");
	


def main():
	
	
	print("---Demonstration of Dir_Wathcers---");
	
	print("Application name: "+argv[0]);
	
	
	if (len(argv)!=2):
		print("Error: invalid numbers of arguments");
		exit();
	
	if (argv[1]== "-h" or argv[1]== "-H"):
		print("This script is used to traverse specific dir");
		exit();
	
	if argv[1]== "-u" or argv[1]=="-U":
		print("usage: ApplicationName AbsolutePath_Of_Directory");
		exit();
	
	try:
		DirectoryWatcher(argv[1]);
	
	except ValueError:
		print("Error: invalid datatype of input");
	
	except Exception:
		print("Error: Invalid input");

if __name__ == "__main__":
	main();
