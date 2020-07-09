'''
4.Write a program which accept one number form user and return addition of its factors.

input: 5
output: 120

'''



def make_factorial(iNo):
	ifact = 1
	
	if iNo <= 0:
		print("invalid input")
		return 0;
	
	while(iNo != 0):
		ifact = ifact * iNo;
		iNo = iNo - 1;
	return ifact;

def main():
	
	ival = int(input("Enter a number: "));
	result = make_factorial(ival);
	
	if result > 0:
		print("Factoria of given num is: ",result)
	else:
		print("try again");


if __name__ == "__main__":
	main();
	
