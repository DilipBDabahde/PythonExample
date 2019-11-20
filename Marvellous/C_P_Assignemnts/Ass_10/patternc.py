'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 3   iCol=4
output:
	  1  1  1  1  1
	  2  2  2  2  2
	  3  3  3  3  3
'''

def patternc(iRow, iCol):
	for i in range(iRow):
		for j in range(iCol):
			print(i+1,end=" ");
		print();


def main():
	irow = int(input("Enter rowsize:"));
	icol = int(input("Enter colsize:"));
	patternc(irow,icol);

if __name__ == "__main__":
	main();
	

