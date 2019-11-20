'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow 4   
	   iCol 3

output: *  *  *
		*  *  *
		*  *  *
		*  *  *
'''


def pattern(irow, icol):
	
	for i in range(irow):
		for j in range(icol):
			print("* ",end=" ");
		print();


def main():

	irow = int(input("Enter row size:"));
	icol = int(input("Enter colsize:"));
	pattern(irow,icol);

if __name__ == "__main__":
	main();
