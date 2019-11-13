'''
Write a program which accept number from user and check
whether that number is strong number or not. When the isum of
the factorial of a number's individual digits are equal to the
number itself, then that number is called a strong number.
Input :  145 since 1! + 4! + 5! = 1 + 24 + 120 = 145
Output : TRUE
'''


def Cheking(iNo):
	temp =iNo;	
	total = 0;

	while iNo != 0:
		digit = int(iNo%10);
		ifact = 1;
		while digit != 0:
			  ifact =ifact * digit;
			  digit = digit - 1;
			  
		total = total + ifact;
		
		iNo = iNo//10;
		
	if total==temp:
		return True;
	else:
		return False;




def main():
	
	val = input("Enter a Num:");
	res = Cheking(int(val));
	if res == True:
		print("Given num is Strong :",res);
	else:
		print("Given num is not Strong:",res);

if __name__ == "__main__":
	main();
		
	#print(__name__);
