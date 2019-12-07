'''
Logic Building Assignment : 12
4. Accept number of rows and number of columns from user and display below pattern.

input: row = 6   col = 5

output: 
		*  *  *  *  *	11 13 14 15 15
		*  @  @  @  *   21 22 23 24 25
		*  @  @  @  *	31 32 33 34 35
		*  @  @  @  *	41 42 43 44 45
		*  @  @  @  *	51 42 43 44 45
		*  *  *  *  *	61 62 63 64 65
'''


def Pattern_Q(row, col):
	
	for i in range(1,row+1):
		for j in range(1,col+1):
			
			if j == 1 or i == 1 or row == i or col == j:
				print("* ",end=" ");
			else:
				print("@ ",end=" ");
		print();


def main():
	
	r_size = int(input("Enter row size: "));
	c_size = int(input("Enter col size: "));
	
	Pattern_Q(r_size, c_size);
	
if __name__ == "__main__":
	main();







		
