'''
7. Write a program which accept one number and display below pattern.

input: 5
output:
		1 2 3 4 5
		1 2 3 4 5
		1 2 3 4 5
		1 2 3 4 5
		1 2 3 4 5

'''

def num_dis_pattern(no):
	if no <= 0:
		print("Invalid input");
		return;

	for i in range(1,no+1):
		for j in range(1,no+1):
			print(j,end=" ")
		print();


def main():
	
	ival = int(input("Enter a number:"));
	
	num_dis_pattern(ival);
	

if __name__ == "__main__":
	main();
	
