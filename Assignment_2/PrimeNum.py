"""
5).Write a program which accept one number for user and check whether number is prime or not.
Input : 5
Output : It is Prime Number
"""

def ChkPrime(iNo):
	i = 0;
	for i in range(2,iNo+1):
		if iNo % i == 0:
			break;			
			
	if i == iNo:
		return True;	
	else:
		return False;
	

def main():
	
	ival = int(input("Enter a val: ",));
	res =ChkPrime(ival);
	
	if res == True:
		print("Given num is Prime");
	else:
		print("Given num is not-Prime");


if __name__ == "__main__":
	main();
