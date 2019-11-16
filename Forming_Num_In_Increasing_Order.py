'''
Accept number from user and return newly formed number which contains all digits in increasing order.

Input  : 61756151
Output : 11155667

Input  : 67807653
Output : 3566778
'''



def Connecting_low_high(iNo):
	
	idigit=0;
	irev=0;
	itemp =0;
	i=0;
	
	while(i<10):
		itemp = iNo
		while(itemp != 0):			
			idigit = itemp % 10;
			if idigit == i:
				irev = irev*10 + idigit;
			itemp = int(itemp/10);		
		i= i + 1;
	return irev;


def main():
	
	ival = int(input("Enter a number: "));
	result = Connecting_low_high(ival);
	print("New formation in increasing order: ",result);
	

if __name__ == '__main__':
	main();
