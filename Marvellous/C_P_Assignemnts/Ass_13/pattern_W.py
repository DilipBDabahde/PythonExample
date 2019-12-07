'''
Logic Building Assignment : 13

Create separate visual Studio project for each problem statement separately.
5)Accept number of rows and number of columns from user and display below pattern.

input: row = 4 
	   col = 4
	   
output:	
	 	1  2  3  4
	 	   2  3  4
	 	   	  3  4
	 	   	  	 4
	  	
'''



def pattern_W(row, col):

	for i in range(1,row+1):
		for j in range(1,col+1):
			if j >= i:
				print(j,end="  ");
			else:
				print(end="   ");
		print();



def main():

 row_Size = int(input("Enter row size: "))
 col_Size = int(input("Enter col size: "))
 
 pattern_W(row_Size, col_Size);

if __name__ == "__main__":
	main();

