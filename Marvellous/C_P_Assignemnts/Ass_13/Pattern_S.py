'''
Logic Building Assignment : 13

Create separate visual Studio project for each problem statement separately.
1)Accept number of rows and number of columns from user and display below pattern.

input: row = 4  
	   col = 4
	   
output:	*				11 12 13 14
		*  *			21 22 23 24
		*  *  *			31 32 33 34
		*  *  *  *		41 42 43 44
'''


def pattern_S(row, col):

	for i in range(1,row+1):
		for j in range(1,col+1):
			if i >= j:
				print("* ",end=" ");
			else:
				pass
		print();



def main():

 row_Size = int(input("Enter row size: "))
 col_Size = int(input("Enter col size: "))
 
 pattern_S(row_Size, col_Size);

if __name__ == "__main__":
	main();

