'''
# wap which two values from user and make multiplication of it using lambda expression

input:  5   8 
output: 40

syntax : 
		lambda(arguments, expression)
'''


fp = lambda a, b: a * b; # anonymous function


def main():
	
	ival1 = int(input("Enter first number: "));
	
	ival2 = int(input("Enter second number: "));
	
	imult = fp(ival1, ival2);  # its like function ptr
	
	print("Multiplication of given values is :",imult);

if __name__ == "__main__":
	main();
	
