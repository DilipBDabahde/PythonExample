'''
5. Accept file name and one string from user and return the frequency of that string from file.
	given file name should be in same directory
Input : Demo.txt	Marvellous
Search 'Marvellous' in Demo.txt
'''

from sys import *;


def Freq_of_str(flname,wakya):	

	fd = open(flname);
	txt = fd.read();	
	#fd.close();
	print("Our file data is: ",txt);
	print("Our string is:",wakya);
	print("Occurance of string in file is: ",txt.count(wakya));
		
	
def main():

	print("Application name: ",argv[0])
	if len(argv) < 3:
		print("Given input is insufficiet");
		print("Input should be like ");
		print("filename and string with cmd line");
		
	else:
		Freq_of_str(argv[1],argv[2]);
	
	

if __name__ == "__main__":
	main();
