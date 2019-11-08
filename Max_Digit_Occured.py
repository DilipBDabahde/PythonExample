'''
3. Accept number from user and return such a digit whose occurrence is maximum.
Input : 67576727
Output: 7

'''

def Max_Occured_Digit(iNo):
	
	a=b=c=d=0;
	x=y=iNo;
	
	while x > 0:
		digit1 = x % 10;
		
		while y > 0:
			digit2 = y % 10;
			if digit1 == digit2:
				a = a + 1;
			y /= 10;
		
		if a > b:
			c =digit1;
			b = a;
		
		a = 0;
		y = iNo;
		
		x /= 10;
	
	return c;


def main():
	
	val = int(input("Enter a val: "));
	Max_Dig = Max_Occured_Digit(val);
	print("Max Occured digit is : ",Max_Dig);
	

if __name__ == '__main__':
	main();
	
