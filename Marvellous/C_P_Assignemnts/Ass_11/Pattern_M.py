'''
Accept number of rows and number of columns from user and display below pattern.
Input : iRow = 5	iCol=5
Output :  1   2   3   4   5
		  2   3   4   5   6
		  3   4   5   6   7
		  4   5   6   7   8
		  5   6   7   8   9
'''


def Pattern_M(irow,  icol):
	
	for i in range(irow):
		x = i+1;
		for j in range(icol):
			print(x, end=" ");
			x = x + 1;
		print();

def main():

	irow = int(input("Enter a rowsize: "));
	icol = int(input("Enter a colsize: "));
	Pattern_M(irow,icol);

if __name__ == "__main__":
	main();
	
