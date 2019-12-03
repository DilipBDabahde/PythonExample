'''
2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py 'Demo' '.txt' '.doc'
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc.


to write script we need to take 
3 paramerts
	 Demo       directory
	 .txt		file extension
	 .doc		file extension
	 
	 wherever we get file with .txt file that we have to convert in .doc format
	 
	 nf = Path(filename).stem + new_ext;
					print(nf);	
					
	
'''

import os 
from sys import *
from pathlib import Path
from os import path

def File_Extension_Modification(path, old_ext, new_ext):

	flag = os.path.isabs(path);	
		
	if flag == False:
		path = os.path.abspath(path);
	
	exists = os.path.isdir(path);	
	
	if exists:
		
		for folder, subFolder, fileList in os.walk(path):
			for filename in fileList:
				if filename.endswith(old_ext):	
					nf = Path(filename).stem + new_ext;
					print(nf);					 
						
	else:
			print("invalid input");
			

def help():
	print("Input should like: DirName .old_ext .new_ext");


def main():
	print("Application Name: ",argv[0]);
	
	if len(argv)!= 4:
		print("Invalid input");
		help();
		exit();
	
	if argv[1]== 'h' or argv[1]== 'H':
		print("This script is use to rename the file extension");
		print("Input should like: DirName .txt .pdf");		
		exit();
	
	if argv[1]== 'u' or argv[1]== '-U':
		print("Usage: Application Req Abspath then we gets files to modify");
		exit();
	
	#try:
		
	File_Extension_Modification(argv[1],argv[2],argv[3]);
	
	#except Exception:
	#	print("Error found",Exception);
	
		
if __name__ == "__main__":
	main();
