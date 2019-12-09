'''
Logic Building Assignment 14
accept row and col from user display below pattern

input: irow = 6 
		icol= 6

output:
	
		*  *  *  *  *  *
		*    		*  *
		*  		 *	   *
		*     *		   *
		*  *		   *
		*  *  *  *  *  *
'''


def PatternAa(irow, icol):

	for i in range(1, irow+1):
		for j in range(1, icol+1):

			if i == 1 or j == 1 or i == irow or j == icol or i + j == icol +1:
				print("* ",end=" ")
			else:
				print("  ",end=" ");
		print()

def main():

	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));

	PatternAa(irow, icol);


if __name__ == "__main__":
	main();