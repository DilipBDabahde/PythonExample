'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 3   iCol=4
output:
	  a  A  a  A
	  b  B  b  B
	  c  C  c  C
	   
'''

def patternd(iRow, iCol):
	
	Cap=65;
	Sml=97;
	for i in range(iRow):			
		for j in range(iCol):
			if j % 2 == 0:
				print(chr(Sml),end=" ");
			else:
				print(chr(Cap),end=" ");
		Sml += 1;
		Cap += 1;	
		print();

def main():
	irow = int(input("Enter rowsize:"));
	icol = int(input("Enter colsize:"));
	patternd(irow,icol);

if __name__ == "__main__":
	main();
	



