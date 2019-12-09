'''
Logic Building Assignment 14
accept row and col from user display below pattern

input: irow = 4 
		icol= 4

output:
		*  *  *  *  *  *  		11  12  13  14  15  15
		*  #  #  #  *  *		21  22  23  24  25  26
		*  #  #  *  &  *		31  32  33  34  35  36
		*  #  *  &  &  *		41  42  43  44  45  46
		*  *  $  $  $  *		51  52  53  54  55  56
		*  *  *  *  *  *		61  62  63  64  64  66
'''


def PatternAa(irow, icol):

	for i in range(1,irow+1):
		for j in range(1,icol+1):

			if i == 1 or j == 1 or i == icol or j == irow or i + j == irow + 1:
				print("* ",end=" ");
			elif  i + j > irow + 1:
				print("$ ",end=" ");
			else:
				print("# ",end=" ");
		print()


def main():

	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));

	PatternAa(irow, icol);


if __name__ == "__main__":
	main();