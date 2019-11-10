'''
accpet num from user and return multiplication of even digit
input: 5291742
outpt: 2*4*2 = 16
'''


def EvenMulti(iNo):
	if iNo == 0:
		return 0;
	
	if iNo < 0:	# modifier
		iNo = -iNo;
		
	mult = 1;
	digit = 0;
	while iNo != 0:
		digit = iNo % 10;
		if digit % 2 == 0:
			mult = mult * digit;
		iNo = iNo // 10;
	
	
	if mult > 1:
		return mult;
	else:
		return 0;


def main():
	val = int(input("Enter a val:"));
	res = EvenMulti(val);
	if res == 0:
		print("There is no even digits in nums");
	else:
		print("Mutli of even nums is: ",res);


if __name__ == '__main__':
	main();
