'''
LBA 15
2. Accept number from user and display below pattern.


input: 5473

output:		5 4 7 3
		  5 4 7
		    5 4 
		      5

'''


def pattern15B(iNo):
	
	itemp = ifact = 0;
	
	while iNo != 0:
		
		itemp = iNo;
		while itemp != 0:
			ifact = ifact * 10 + itemp % 10;
			itemp = int(itemp/10);
		
		
		while ifact != 0:
			print(ifact%10,end=" ");
			ifact = int(ifact/10);
		
		iNo = int(iNo/10);
		print();	
		
def main():
	
	ival = int(input("Enter number "));
	
	pattern15B(ival);


if __name__ == "__main__":
	main();
