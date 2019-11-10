'''
4.Write a recursive program which accept number from user and return summation of its digits.
Input : 879
Output : 24
'''
isum = 0;
def DigitSum(iNo):
	global isum;
	if iNo != 0:
		isum = isum + iNo % 10;
		DigitSum(iNo = iNo // 10);
		
	return isum;


def main():
	val = int(input("Enter a val:"));
	res = DigitSum(val);
	print("some of all dijits is: ",res);

if __name__ == '__main__':
	main();
