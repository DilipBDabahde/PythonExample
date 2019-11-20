'''
Accept number from user and return newly formed number which contains all
digits in decreasing order.
Input  : 61756151
Output : 76655111

Input  : 67807653
Output : 8776653
'''

def NewNum(iNo):
	icnt = 9;
	sum = 0;
	itemp = iNo;
	while icnt >= 0:		
		itemp = iNo;
		while itemp != 0:
			if icnt==int(itemp%10):		
				sum = sum*10+icnt;
			itemp = int(itemp/10);
		icnt = icnt - 1;
	
	return sum;
	

def main():

	ival = int(input("Enter a val: "));
	res = NewNum(ival);
	print("After new formation of given num :",res);


if __name__ == "__main__":
	main();
