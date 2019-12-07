'''
Logic Building Assignment : 13

Create separate visual Studio project for each problem statement separately.
4)Accept number of rows and number of columns from user and display below pattern.

input: row = 6  
	   col = 6
	   
output:	
	   	*  *  *  *  *  *
		*  *           *
		*     *		   *
		*	     *	   *
		*			*  *	
		*  *  *  *  *  *
	  	
'''



def pattern_S(row, col):

	for i in range(1,row+1):
		for j in range(1,col+1):
			if i == j or i == 1 or j == 1 or row == i or col == j:
				print("*\t",end=" ");
			else:
				print("\t",end=" ");
		print();



def main():

 row_Size = int(input("Enter row size: "))
 col_Size = int(input("Enter col size: "))
 
 pattern_S(row_Size, col_Size);

if __name__ == "__main__":
	main();

