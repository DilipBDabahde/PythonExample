"""
8.Write a program which accept number from user and print that number of “*” on screen.
Input : 5
Output : * * * * *
"""


import sys;

def PrintStar(iNo):
	
	while iNo > 0:
		print("* ","",end="");
		iNo -= 1;
	
def main():

	ival = int(sys.argv[1]);	#taking input from user using command line argument
	PrintStar(ival);
	print("");
	

if __name__ == "__main__":
	main();
