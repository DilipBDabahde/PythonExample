'''
.Write a program which accept one number from user and return
smallest digit.
Input  : 712
Output : 1
Input  : 7520
Output : 0
'''

def ChkSmallestDigit(iNo):
	sml = iNo % 10;
	
	while iNo != 0:
		digit = iNo % 10;
		if digit < sml:
			sml = digit;
		
		iNo = int(iNo / 10);
	
	return sml;

def main():
	val = int(input("Enter a Num:"));
	res = ChkSmallestDigit(val);
	print("Small digit is: ",res);	

if __name__ =="__main__":
	main();
