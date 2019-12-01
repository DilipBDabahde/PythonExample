'''
3.Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from 
existing file into new file. Accept file name through command line arguments.

Input : ABC.txt Demo.txt
means we have to given first file name which is new and second name should be exiting file name
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

Demo.txt is Existing file
ABC.txt is new file
'''

import sys,os


def Cpy_ExistsFile_To_NewFile(NFile,existfile):
	

	with open(existfile,'r')as fobj:
		txt=fobj.read();		
		fobj.close();
		
	with open(NFile,'w') as cp:
		cp.write(txt);
		cp.close();
	
	with open(NFile,'r')as rd:
		print("after cpy :--> "+rd.read());
		rd.close();		



def main():
	
	print("Application name: ",sys.argv[0]);
	print("New file name: ",sys.argv[1]);
	Cpy_ExistsFile_To_NewFile(sys.argv[1],sys.argv[2]);
	


if __name__ == "__main__":
	main();
	
