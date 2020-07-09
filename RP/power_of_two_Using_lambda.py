'''
write a program which accept one num from user and return power of two  , for the given number
input: 7
ouput: 49		power of tow
'''

# using lambda function we return power of two

fp =  (lambda no : no ** 2)



def main():
	
	val = int(input("Enter a number: "));
	
	result = fp(val);
	
	if result > 0:
		print("Power of given number is: ",result);
	else:
		print("Something wrong try again:");


if __name__ == "__main__":
	main();
	
