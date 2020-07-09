'''
4.Write a program which accept one number form user and return addition of its factors.

input: 12	output: 1+2+3+4+6 = 16

12 is div by all 1+2+3+4+6 these nums

so that this are factors of 12 except 12

'''


def factors_addition(no):
	
	isum = 0;
	i = 0;
	
	for i in range(1,no+1//2):
		if no % i == 0:
			isum = isum + i;
		
	
	return isum;


def main():
	
	ival = int(input("Enter a Number: "));
	result = factors_addition(ival);
	
	if result > 0:
		print("Given Number Factors Sum is: ",result);
	else:
		print("Try again");

if __name__ == "__main__":
	main();
	
