'''
Logic Building Assignment : 13

Create separate visual Studio project for each problem statement separately.
3)Accept number of rows and number of columns from user and display below pattern.

input: row = 5  
	   col = 5
	   
output:	
		$  *  *  *  * 
		#  $  *  *  *
		#  #  $  *  *		
		#  #  #  $  *
		#  #  #  #  $		
'''



def pattern_S(row, col):

	for i in range(1,row+1):
		for j in range(1,col+1):
			if i == j:
				print("$ ",end=" ");
			elif i > j:
				print("# ",end=" ");
			else:
				print("* ",end=" ");
		print();



def main():

 row_Size = int(input("Enter row size: "))
 col_Size = int(input("Enter col size: "))
 
 pattern_S(row_Size, col_Size);

if __name__ == "__main__":
	main();

