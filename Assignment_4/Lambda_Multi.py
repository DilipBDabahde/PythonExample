'''
2).Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3
Input : 6 3
Output : 12
Output : 18
'''


fun = lambda iNo1,iNo2: iNo1*iNo2;


def main():
	
	val1 = input("Enter Val1: ");
	val2 = input("Enter Val2: ");
	
	result = fun(int(val1),int(val2));
	
	print("Multi is :",result);
	
if __name__ == "__main__":
	main();
