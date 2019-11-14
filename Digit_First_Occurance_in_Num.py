'''
. Accept number and one digit from user and return first occurrence of that digit.
Input  : 6757347	7
Output : 2 
Input  : 6757347	3
Output : 5 
Input  : 6757347	1
Output : -1 
'''


def FirstOccured(iNo,fnd_dig):
	
	irev = 0;
	idigit=0;
	icnt=0;
	ihold=0;
	
	if iNo < 0:
		return -1;
	
	
	while iNo != 0:
		idigit = iNo % 10;
		irev = irev * 10 + idigit;
		iNo = int(iNo / 10);
	
	while irev != 0:
		idigit = irev%10;
		icnt = icnt + 1;
		if idigit == fnd_dig:
			ihold = icnt;
			break;
		irev = int(irev/10);
	
	
	return ihold;
		


def main():
	num = int(input("Enter a val: "));
	digit = int(input("Enter digit: "));
	result = FirstOccured(num,digit);

	if result == -1:
		print("invlid input");
	elif result >= 0:
		print("First occurance of [",digit,"] is [",result,"] at index");
 	
 	
 	
 	
if __name__ == '__main__':
	main();
