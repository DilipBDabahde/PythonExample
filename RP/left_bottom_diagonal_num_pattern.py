'''
8. Write a program which accept one number and display below pattern.

input:  5
output:
		
		1
		1	2
		1	2 	3
		1	2	3	4
		1	2	3	4	5

'''


def left_bottom_diagonal_num_pattern(no):
	
	if no <= 0:
		print("invalid input");
		return;
	
	
	for i in range(1,no+1):
		for j in range(1, i+1):
			print(j, end=' ');
		print();


def main():
	
	ival = int(input("Enter a number: "));
	
	left_bottom_diagonal_num_pattern(ival);
	

if __name__ == '__main__':
	main();
	
