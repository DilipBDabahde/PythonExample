'''
Accept number of rows and number of columns from user and display below pattern.
Input : iRow = 5	iCol=5
Output :  1   2   3   4   5
		 -1  -2  -3  -4  -5
		  1   2   3   4   5
		 -1  -2  -3  -4  -5
		  1   2   3   4   5
'''



def Pattern_L(irow, icol):

	for i in range(irow):
		for j in range(icol):
			if i % 2 == 0:
				print(j+1,end="  ");
			else:
				print(-(j+1),end=" ");
		print();
		

def main():

	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));
	
	Pattern_L(irow, icol);


if __name__ == "__main__":
	main();

