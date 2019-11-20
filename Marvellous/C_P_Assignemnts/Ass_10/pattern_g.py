'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow = 3   iCol=5
output:
	  1  #  2  #  3
	  1  #  2  #  3
	  1  #  2  #  3
	   
'''

def pattern_g(iRow, iCol):
		
		for i in range(1,iRow+1):
			x = 1;
			for j in range(1,iCol+1):
				if j % 2 == 0:
					print("#",end=" ");
				else:
					print(x,end=" ");
					x += 1;
			print();		
		
		
def main():
	irow = int(input("Enter rowsize:"));
	icol = int(input("Enter colsize:"));
	pattern_g(irow,icol);

if __name__ == "__main__":
	main();
	



