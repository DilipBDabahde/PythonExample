"""
7).Write a program which accept one number and display below pattern.
Input :
5
Output : 1 2 3 4 5
	 1 2 3 4 5
	 1 2 3 4 5
	 1 2 3 4 5
	 1 2 3 4 5
"""


def Pattern3(iNo):

	for i in range(0,iNo):
		for j in range(0,iNo):
			print(j+1,"",end='');
		print('');


def main():
	
	ival = int(input("Enter a val: "));
	Pattern3(ival);


if __name__ == "__main__":
	main();
