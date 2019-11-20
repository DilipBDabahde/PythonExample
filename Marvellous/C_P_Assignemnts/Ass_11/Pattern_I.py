'''
Accept number of rows and number of columns from user and display below pattern.

input: irow=4    icol=4

output:	1  2  3  4 
		5  6  7  8
		9  1  2  3
		4  5  6  7
'''



def pattern_I(irow, icol):
	x = 1;
	for i in range(irow):		
		for j in range(icol):
			if x <= 9:
				print(x,end=" ");
				x = x + 1;
				if x == 10:
					x=1;

		print();
	

def main():
	rowsize= int(input("Enter a row size: "));
	colsize= int(input("Enter a col size: "));
	pattern_I(rowsize,colsize);


if __name__ == "__main__":
	main();
