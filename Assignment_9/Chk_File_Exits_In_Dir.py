'''
1.Write a program which accepts file name from user and check whether that file exists in current directory or not.
'''

import os;
import sys;





def Chk_File_Exists(fname):

	 if os.path.exists(fname):
	 	print("File exits");
	 else:
	 	print("File does not exits");

def main():
	
	print("Application name: "+sys.argv[0]);
	Chk_File_Exists(sys.argv[1]);	
	

if  __name__ == "__main__":
	main();
