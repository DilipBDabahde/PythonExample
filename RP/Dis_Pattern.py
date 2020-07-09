'''
2. Write a program which accept one number and display below pattern.
input: 5	
output:	*	*	*	*	*
		*	*	*	*	*
		*	*	*	*	*
		*	*	*	*	*
		*	*	*	*	*
'''

def display_Pattern(no):
	
	if no <= 0:
		print("Invalid input");
	
	for i in range(1, no+1):
		for j in range(1, no+1):
			print("*",end=" ");
		print("");


if __name__ == "__main__":
	ival = int(input("Enter number: "));
	display_Pattern(ival);
