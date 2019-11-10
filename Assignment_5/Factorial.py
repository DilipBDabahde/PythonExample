'''
5. Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120
'''

i = fact = 1;

def factorial(iNo):
	global i;
	global fact;

	if i <= iNo:
		fact *= i;
		i = i + 1;
		factorial(iNo);
	
	return fact;


def main():
	
	val = int(input("Enter a val:"));
	res = factorial(val);
	print("factorial of given num is :",res);



if __name__ == "__main__":
	main();

