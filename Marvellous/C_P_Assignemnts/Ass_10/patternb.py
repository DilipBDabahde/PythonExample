'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 3   iCol=4
output: 
		*  #  *  #
		*  #  *  #
		*  #  *  #
'''


def patternb(iRow, iCol):
	for i in range(iRow):
		for j in range(iCol):
			if (j+1) % 2 == 0:
				print("#", end=" ");
			else:
				print("* ",end=" ");
		print();


def main():

	irow = int(input("Enter rowsize: "));
	icol = int(input("Enter colsize: "));
	patternb(irow,icol);

if __name__ == "__main__":
	main();
		
