"""
3.Write a program which contains one function named as Add() which accepts two numbers from user and return 
addition of that two numbers.

Input : 11 5
Output : 16
"""


def Add(No1, No2):
	Ans = 0;
	Ans = No1 + No2;
	return Ans;


import sys;
def main():
	
	val1 = int(sys.argv[1]);
	val2 = int(sys.argv[2]);
	
	result = Add(val1, val2);
	print("Addition of two nums is :",result);



if __name__ == "__main__":
	main();
