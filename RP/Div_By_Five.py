'''
Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.

input: 8		output: FALSE
input: 25		output: TRUe
'''


def div_by_five(no):
	if no % 5 == 0:
		print("TRUE");
	else:
		print("FALSE");

if __name__ == "__main__":
	
	ival = int(input("Enter Number: "));
	div_by_five(ival);

