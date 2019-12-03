'''
1.Design automation script which accept directory name and file extension from user. Display all files with that extension.
Usage : DirectoryFileSearch.py Demo   .txt
Demo is name of directory and .txt is the extension that we want to search.


in this program we are taking two command line argv as directory name and extention of file 
given helper fuction will give  use all .extention files from the currect directory
'''


'''
import os
for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
'''


from sys import *
import os

def sameExtension(path, extension):
		
		
		flag = os.path.isabs(path);	# this fun us to check given parameter has abs path or not
		
	
		if flag == False:			# if flag is False then given path is not abs then we need to modify with below
			path = os.path.abspath(path);	#path conversion
		
		exists = os.path.isdir(path); # after modification if path is conts directory it contaisn True else false
		
		if exists:
			print("Given path is valid");
			
			for folder, subFolder, fileList in os.walk(path):
				#print("Current Directory Name : ",folderLst);
				for filename in fileList:
					if filename.endswith(extension):
						print(os.path.join(folder,filename));
					
		else:
			print("Given path is invalid");
	
	
	
def main():

	print("Application Name:"+argv[0]); #this will display our file name
	print("Length of given cmd arg",len(argv));
	
	if len(argv)!=3:
		print("Given input is Invalid");
		exit();
		
	if argv[1]=="-h" or argv[1]=="-H":
		print("This script is used to display perticular format files");
		exit();
	
	if argv[1]=='-u' or argv[1]=='-U':
		print("Usage: Application is used to Display same format files from given Directories");
		exit();
	
	try:			
		sameExtension(argv[1],argv[2]);
	
	except ValueError :
			print("File Nof found");
	
	except Exception:
		print("invalid input",Exception);
		


if __name__ == "__main__":
	main();

