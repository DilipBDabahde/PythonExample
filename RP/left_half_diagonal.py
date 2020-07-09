'''
Write a program which accept one number and display below pattern
input: 5
output:
		*	*	*	*	*
		*	*	*	*
		*	*	*
		*	*
		*
'''


def left_half_diagonal(no):
	
	if no <= 0:
		print("invalid input");
	
	for i in range(1,no+2):
		for j in range(1,((no+2)-i)):
			print("*",end=" ");
		
		if i != no:
			print();


def main():
	
	ival = int(input("Enter  a Number: "));
	
	# function calling with one argument known as positional arguments
	
	left_half_diagonal(ival);
	

if __name__ == "__main__":	#__name__ is global variable which contains string as "__main__" if its true then get in
	
	main(); # calling to main fuction from here
	
