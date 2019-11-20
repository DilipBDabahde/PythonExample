'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 3   iCol=5
output:
	  1  2  3  4  5
	  6	 7  8  9  10
	  11 12 13 15 16	   
'''


def Pattern_H(iRow,iCol):
	x = 1;
	for i in range(iRow):
		for j in range(iCol):
			print(x,end=" ");
			x += 1;
		print();
		
def main():
	irow = int(input("Enter row size:"));
	icol = int(input("Enter colsize: "));
	Pattern_H(irow,icol);


if __name__ == "__main__":
	main();
