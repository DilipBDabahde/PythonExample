'''
2. Write a program which accept file name from user and open that file and display the contents  of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.
'''

import sys
import os

def fname(filename):
	if os.path.exists(filename):
		fopen = open(filename,'r');
		print(fopen.read());
	else:
		print("File does not exits");	

def main():

	print("Application name: ",sys.argv[0]);
	print("File name: ",sys.argv[1]);
	
	fname(sys.argv[1]);


if __name__ == "__main__":
	main();
