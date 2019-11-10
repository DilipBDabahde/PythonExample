'''
1. Write a recursive program which display below pattern.
Input : 5
Output : * * * * *
'''


def Star(iNo):
	if iNo != 0:
		iNo = iNo - 1;
		Star(iNo);
		print("*",end=" ");

def main():

	val = int(input("Enter a val:"));
	Star(val);
	print();

if __name__ == '__main__':
	main();
