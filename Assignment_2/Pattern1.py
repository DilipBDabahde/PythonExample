"""
2)Write a program which accept one number and display below pattern.

Input : 5

Output :* * * * * 
	* * * * *
	* * * * *
	* * * * *
	* * * * *
	
	use Command line argument
"""

import sys;

def Pattern1(iNo):
	
	for i in range(0,iNo):
		for j in range(0,iNo):
			print("* ","",end="");
		print("");


def main():
	
	ival = int(sys.argv[1]);
	Pattern1(ival);


if __name__ == "__main__":
	main();
	
