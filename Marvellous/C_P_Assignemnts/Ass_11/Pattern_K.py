'''
Accept number of rows and number of columns from user and display below pattern.
input : irow = 5  icol = 5
		
		a  b  c  d  e
		1  2  3  4  5
		a  b  c  d  e
		1  2  3  4  5
		a  b  c  d  e
'''

def Pattern_K(irow, icol):
	
	for i in range(irow):
		ch = 97;	
		for j in range(icol):
			if i % 2 == 0:
				print(chr(ch),end=" ");
				ch = ch + 1;
			else:
				print(j+1,end=" ");
		print();



def main():
	
	irow = int(input("Enter rowsize: "));
	icol = int(input("Enter colsize: "));
	Pattern_K(irow, icol);

if __name__ == "__main__":
	main();
