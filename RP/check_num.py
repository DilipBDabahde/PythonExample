'''
Write a program which accept number from user and check whether that number is positive or
negative or zero

input: 90   output: Positive
input: -123	output: Negative
input: 0  	output: Zero

'''

def check(no):
	
	if no > 0:
		print("Positive Number");
	elif no < 0:
		print("Negative Number");
	elif no == 0:
		print("Zero");

if __name__ == "__main__":
	
	ival = int(input("Enter Number: "))
	check(ival);





