'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 4   iCol=4
output:
	  A  B  C  D
	  a	 b  c  d
	  A  B  C  D
	  a	 b  c  d 
'''

def patternd(iRow, iCol):
	
	for i in range(iRow):
		Cap=65;
		Sml=97;
		for j in range(iCol):
			if i % 2 == 0:
				print(chr(Cap),end=" ");
				Cap += 1;
			else:
				print(chr(Sml),end=" ");
				Sml += 1;		
		print();

def main():
	irow = int(input("Enter rowsize:"));
	icol = int(input("Enter colsize:"));
	patternd(irow,icol);

if __name__ == "__main__":
	main();
	



