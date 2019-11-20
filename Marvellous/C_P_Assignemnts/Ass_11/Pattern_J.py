'''
Accept number of rows and number of columns from user and display below pattern.
input: irow=4   icol=5

output:  2  4  6  8  10
		 1  3  5  7  9
		 2  4  6  8  10
		 1  3  5  7  9
'''

def pattern_J(irow, icol):
	
	for i in range(1,1+irow):
		for j in range(1,1+icol):
			if i % 2 != 0:
				print(j+j,end=" ");
			else:
				print((j+j)-1,end=" ");
		print();


def main():
	
	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));
	pattern_J(irow, icol);


if __name__ == "__main__":
	main();
	 


		 
