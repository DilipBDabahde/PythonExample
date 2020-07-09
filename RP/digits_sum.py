'''
10. Write a program which accept number from user and return addition of digits in that number.

input: 2323
output: 10

input: 10
output: 1

'''


def digit_sum(no):
	
	isum = 0;
	
	while(no != 0):
		
		isum = isum + (no % 10);
		no = no // 10;
	
	
	return isum;


def main():
	
	ival = int(input("Enter a number: "));
	result = digit_sum(ival);
	
	print("Sum of all digits is: ",result);


if __name__ == "__main__":
	main();
	
