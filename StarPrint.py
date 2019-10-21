"""
accept num from user and print that num of 8 on screen use for,while
input:5
output: * * * * * 

input: 3
output: * * *

input:0
output: ___
"""

import sys;

def ForUse(iNo):
	print("using for loop");
	for i in range(0,iNo):
		print("* ",end="");
	print("");


def WhileUse(iNo):
	print("using while loop");
	while iNo > 0:
		print("* ",end="");
		iNo-=1;
	print("");


def main():
	ival = int(sys.argv[1]);
	ForUse(ival);
	WhileUse(ival);
	

if __name__=='__main__':
	main();
 

