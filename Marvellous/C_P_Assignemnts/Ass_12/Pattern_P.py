'''
Logic Building Assignment : 12

2. Accept number of rows and number of columns from user and  display below pattern.

input: row = 4    column= 4

output: *  *  *  *		11 12 13 14 
		*  *  *  #		21 22 23 24 
		*  *  #  #		31 32 33 34 
		*  #  #  #		41 42 43 44 
						
'''

def Pattern_P(row, col):
	
	for i in range(1,row+1):
		for j in range(1,col+1):
			if i+j > ((row+col)/2)+1:
				print("# ",end=" ");
			else:
				print("* ",end=" ");
		print();



def main():
	
	r_size = int(input("Enter row size: "));
	c_size = int(input("Enter col size: "));
	
	Pattern_P(r_size, c_size);
	
if __name__ == "__main__":
	main();
