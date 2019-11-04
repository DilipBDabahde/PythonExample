'''
1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
'''
	
fp = lambda iNo: (iNo**2);


def main():
	
	iNo = input("Enter a Val: ");
	
	res = fp(int(iNo));
	print("power of given num is: ",res);


if __name__ == "__main__":
	main();
