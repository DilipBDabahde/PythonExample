'''
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers

input: 10  5		output: 15
input: 4   8		output: 12

'''

def Add(no1, no2):
	ans = no1 + no2;
	return ans;


if __name__ == "__main__":

	ival1 = int(input("Enter first num: "));
	ival2 = int(input("Enter second num: "));
	
	result = Add(ival1, ival2);
	
	print("Addition of given values is: ", result);


