'''
5.Write a program which accept one number for user and check whether number is prime or not.

input: 5 
output: Its Prime

input: 6
output: Its not Prime

5 is prime bcs this num is divisible by 1 and 5 not others
and also known as divisible by 1 and itself

6 is not prime bcs it is div by 1, 2, 3 and itself
so here 2 and 3 these nums are included to make complete division of 6 so that, we can not consider it as prime num

'''

def check_prime(no):
	
	if no <= 0:
		print("Invalid input");
		return 0;
	
	icnt = 0;
	
	for i in range(2, no+1//2):
		if no % i == 0:
			icnt = icnt + 1;
		
	if icnt > 0:
		return False;
	else:
		return True;
		

def main():
	
	iNo = int(input("Enter a number:"))
	
	result = check_prime(iNo);
	if result == True:
		print(iNo," is prime Number");
	else:
		print(iNo," is not prime number");
	

if __name__ == "__main__":
	main();
	
