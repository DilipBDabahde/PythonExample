"""
9).Write a program which accept number from user and return number of digits in that number.
Input : 5187934
Output : 7

"""

def CntDigits(iNo):
	icnt = 0;
	while iNo > 0:
		#idigit = iNo % 10;
		icnt += 1;
		iNo = iNo//10;
	
	return icnt;


def main():
	
	ival = int(input("Enter a val:"));
	res = CntDigits(ival);
	print("Total Digits are : ",res);
	

if __name__ == "__main__":
	main();
