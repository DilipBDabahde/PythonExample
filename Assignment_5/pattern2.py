'''
3.Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
'''


def pattern2(iNo):
	if iNo != 0:
		print(iNo,end=" ");
		iNo -= 1;
		pattern2(iNo);

def main():
	val = int(input("Enter a val:"));
	pattern2(val);
	print();
	
if __name__ == '__main__':
	main();
