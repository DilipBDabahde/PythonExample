'''
LBA 15
1. Accept number from user and display below pattern.

input:  5473
	
output:
		5  4  7  3
		3  7  4  5
		5  4  7  3
		3  7  4  5

'''




def Pattern15A(iNo):
	
	itemp = iNo;
	icnt = ival = digit = ifact =0
	
	while iNo != 0:
		
		idigit = iNo % 10;
		ifact = ifact * 10 + idigit;
		iNo = int(iNo/10);
		icnt = icnt + 1;
	
	iNo = itemp;
	
	while icnt != 0:
		
		if icnt % 2 != 0:
			
			ival = ifact;
			while ival != 0:
				digit = ival % 10;
				print(digit,end = " ");
				ival = int(ival/10);
		else:
			ival = iNo;
			while ival != 0:
				idigit = ival % 10;
				print(idigit, end=" ");
				ival = int(ival/10);
		
		print(" ");
		icnt = icnt - 1;	


def main():
	
	
	Num = int(input("Enter a num: "));
	
	Pattern15A(Num);



if __name__ == "__main__":
	main();
	

