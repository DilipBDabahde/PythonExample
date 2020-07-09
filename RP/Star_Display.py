'''
write  a program which accept number from user and print that number of “*” on screen.
input: 5
output: *  *  *  *  *
'''

def star_display(no):
	if no <= 0:
		print("No more traval");
		return;
	
	for i in range(0, no):
		print("* ",end='');
	
	print();


if __name__ == "__main__":
	
	ival = int(input("Enter Number: "));
	
	star_display(ival);
