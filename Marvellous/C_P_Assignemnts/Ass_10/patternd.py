'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 4   iCol=4
output:
	  A  B  C  D
	  A  B  C  D
	  A  B  C  D
	  A  B  C  D 
'''

def patternd(iRow, iCol):
	
	for i in range(iRow):
		c=65;
		for j in range(iCol):
			print(chr(c),end=" ");
			c += 1;
		print();

def main():
	irow = int(input("Enter rowsize:"));
	icol = int(input("Enter colsize:"));
	patternd(irow,icol);

if __name__ == "__main__":
	main();
	



