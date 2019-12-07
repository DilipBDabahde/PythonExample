'''
Logic Building Assignment : 12

1. Accept number of rows and number of columns from user and  display below pattern.

input: row = 4    column= 4

output: *  #  #  #		11 12 13 14
		*  *  #  #		21 22 23 24
		*  *  *  #		31 32 33 34
		*  *  *  *		41 42 42 44

'''




def PatternAA(row, col):
	
	#print(row, col);
	
	for i in range(row):
		for j in range(col):
			if (i < j):
				print("# ",end=" ");
			else:
				print("* ",end=" ");
		print();



def main():
	
	r_size = int(input("Enter row size: "));
	c_size = int(input("Enter col size: "));
	
	PatternAA(r_size, c_size);
	

if __name__ == "__main__":
	main();
