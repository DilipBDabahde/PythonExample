'''
Logic Building Assignment 14
accept row and col from user display below pattern

input: irow = 4 
		icol= 4

output:
		1  2  3  4  5  6  		11  12  13  14  15  15
		1  2           6		21  22  23  24  25  26
		1     3        6		31  32  33  34  35  36
		1        4     6		41  42  43  44  45  46
		1           5  6		51  52  53  54  55  56
		1  2  3  4  5  6		61  62  63  64  64  66
'''


def PatternAa(irow, icol):

	for i in range(1,irow+1):
		for j in range(1,icol+1):

			if i == j:
				print(i,end=" ")
			elif i == 1 or i == icol:
				print(j,end=" ")
			elif j == 1:
				print(j, end=" ");
			elif j == irow:
				print(j,end=" ");
			else:
				print(" ",end=" ")				
		print()


def main():

	irow = int(input("Enter row size: "));
	icol = int(input("Enter col size: "));

	PatternAa(irow, icol);


if __name__ == "__main__":
	main();