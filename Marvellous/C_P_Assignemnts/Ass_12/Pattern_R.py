'''
Logic Building Assignment : 12
5. Accept number of rows and number of columns from user and display below pattern.

input: row = 6   col = 5

output: 
   j--> 1  2  3  4  5	11 12 13 14 15
		1  @  @  @  5   21 22 23 24 25
		1  @  @  @  5	31 32 33 34 35
		1  @  @  @  5	41 42 43 44 45
		1  @  @  @  5	51 42 43 44 45
		1  2  3  4  5	61 62 63 64 65
  i-----^
		
'''

def Pattern_R(row, col):
	
	for i in range(1,row+1):
		for j in range(1,col+1):			
			
			if i == 1 or j == 1:
				print(j,end=" ");
			elif i == row or j == col:
				if i == row:
					print(j,end=" ");
				else:
					print(col,end=" ")
			else:
				print("@",end=" ");
		print();


def main():
	
	r_size = int(input("Enter row size: "));
	c_size = int(input("Enter col size: "));
	
	Pattern_R(r_size, c_size);
	
if __name__ == "__main__":
	main();


		
