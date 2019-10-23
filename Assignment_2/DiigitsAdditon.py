"""
10).Write a program which accept number from user and return addition of digits in that number.
Input : 5187934
Output : 37
"""

import sys;

def DigitsAddition(iNo):
	sum = 0;
	while iNo > 0 :
		idigit = iNo % 10;
		sum = sum + idigit;
		iNo = iNo // 10;
		
	return sum;	 
	 
def main():
	
	ival = int(sys.argv[1]);
	res = DigitsAddition(ival);
	
	print("Addition of all Digits is : ",res);


if __name__ == "__main__":
	main();
