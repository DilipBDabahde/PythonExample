'''
9. Write a program which accept number from user and return number of digits in that number.

input: 3235545
output: 7

input: 10
output: 2
'''


def count_digits(no):
	
	icnt = 0;
	
	while no != 0 :
		no = no//10;
		icnt = icnt + 1;
	
	return icnt;


def main():
	
	ival = int(input("Enter number: "));
	
	result = count_digits(ival);
	
	print("Number of digits are: ", result)



if __name__ == "__main__":
	main();
