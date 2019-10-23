"""
6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11
Output : Positive Number

Input : -8
Output : Negative Number

Input : 0
Output : Zero

use command line argument;;;;;;;;;;

"""



import sys;

def ChkNum(iNo):

	if(iNo > 0):
		print("Given Number is Positive");
	elif(iNo < 0):
		print("Given Number is Negative");
	else:
		print("Given Number is Zero");


def main():
	
	ival = int(sys.argv[1]);
	ChkNum(ival);

if __name__ == "__main__":
	main();

