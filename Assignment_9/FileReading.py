'''
2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.
'''


import os
import sys 
'''
def Open_file(flname):
	
	

		fb = open("/home/dilip/Programming/Python/flname",'r');
		print(fb);
		print(fb.read())



def main():

	print("Application name: ",sys.argv[0]);
	print("File name: ",sys.argv[1]);
	Open_file(sys.argv[1]);

if __name__ == "__main__":
	main();

'''

fd = open("Demo.txt",'r');
print(fd)
print(fd.read());
