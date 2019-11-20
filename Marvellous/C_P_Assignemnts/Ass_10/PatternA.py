'''
Accept number of rows and number of columns from user and display below pattern.
Input : iRow = 3   iCol=5
output:
		1 2 3 4 5
		5 4 3 2 1
		1 2 3 4 5
'''


def PatternA(iRow, iCol):
	for i in range(iRow):
		if (i+1)%2 == 0:
			temp = iCol;
			while temp != 0:
				print(temp, end=" ");
				temp -=1;
		else:
			for j in range(iCol):
				print(j+1,end=" ");
		print();


def main():
	
	row = int(input("Enter row size: "));
	col = int(input("Enter col size: "));
	PatternA(row, col);


if __name__ == "__main__":
	main();
						

