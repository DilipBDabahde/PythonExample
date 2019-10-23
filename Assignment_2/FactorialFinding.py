"""
3).Write a program which accept one number from user and return its factorial.
Input :
5
Output : 120
"""


def Factorial(iNo):
	
	ifact = 1;
	for i in range(1,iNo+1):
		ifact *= i;
	return ifact;


def main():
	
	ival = int(input("Enter a val: "));
	res = Factorial(ival);
	print("Factorial of given num is: ",res);


if __name__ =="__main__":
	main();
