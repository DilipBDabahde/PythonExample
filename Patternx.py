'''
Accept number from user and print below pattern.
Input : 4
Output : * * * * # # # #
'''

def PatternNew(iNo):
	
	for i in range(iNo*2):
		if i < iNo:
			print("*",end=" ");
		else:
			print("#",end=" ");


def main():
	
	val = int(input("Enter a val:"));
	PatternNew(val);
	print();


if __name__ =="__main__":
	main();
