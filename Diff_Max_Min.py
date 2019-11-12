'''
Accept three numbers from user and return difference between largest and smallest digit.
Input : 543
Output: 2 (5 - 3)
Input : 7309
Output: 9 (9 - 0)
Input : 7319
Output: 8 (9 - 1)
'''

def Max_Min_Diff(iNo):
	imin=imax= iNo % 10;
	
	while iNo != 0:
		digit = iNo % 10;
		if digit < imin:
			imin=digit;
		
		if digit > imax:
			imax=digit;
		iNo = iNo//10;
	
	return imax - imin;


def main():
	
	val = int(input("Enter a val: "));
	res = Max_Min_Diff(val);
	print("Diff from max and min digits is: ",res);
	

if __name__ == "__main__":
	main();
