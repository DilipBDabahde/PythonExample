"""
6).Write a program which accept one number and display below pattern.
Input: 5
Output: * * * * *
	* * * *
	* * *
	* *
	*
"""



def Pattern2(iNo):
	
	for i in range(0,iNo):
		for j in range(0,iNo-i):
			print("* ","",end="");
		print("");
			

def main():
	
	ival = int(input("Enter a val: "));
	Pattern2(ival);
	

if __name__ == "__main__":
	main();
