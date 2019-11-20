'''
Accept number of rows and number of columns from user and display below pattern.

input: iRow 4   
	   iCol 3

output: 1  2  3
		1  2  3
		1  2  3 
		1  2  3
'''

def NumPat(iRow, iCol):
	for i in range(iRow):
		for j in range(iCol):
			print(j+1,end=" ");
		print();


def main():

	irow = int(input("Enter row size:"));
	icol = int(input("Enter col size:"));
	NumPat(irow, icol);


if __name__ == "__main__":
	main();
