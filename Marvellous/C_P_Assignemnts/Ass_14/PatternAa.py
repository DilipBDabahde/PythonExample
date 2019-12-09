'''
accept row and col from user display below pattern

input: irow = 4 
		icol= 4

output:
	
		*  *  *  #		11 12 13 14
		*  *  #  *		21 22 23 24
		*  #  *  *		31 32 33 34
		#  *  *  *		41 42 43 44
'''


def PatternAa(irow, icol):

	for i in range(1, irow+1):
		for j in range(1, icol+1):
			if i + j == irow + 1:
				print("#  ",end=" ");
			else:
				print("*  ",end=" ");
		print();



def main():

	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));

	PatternAa(irow, icol);


if __name__ == "__main__":
	main();