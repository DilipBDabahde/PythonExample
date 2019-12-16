'''
accept list from user and display factorial of each elements

input: N  4
		  6    3   4   9
		  720  6   24  362880
'''


def DisplayFactorial(arr):
	
	brr = [];
	ifact = 0
	itemp = 0
	print(arr);
	for i in range(len(arr)):
		
		ifact = 1
		itemp = arr[i];
		while itemp != 0:
			ifact = ifact * itemp;
			itemp = itemp - 1;
		
		brr.append(ifact);
	print(brr);


def main():
	
	 size = int(input("Enter list size: "));
	 arr = [];
	 for i in range(size):
	 	arr.append(int(input("Enter num:")));
	 
	 DisplayFactorial(arr);

if __name__ == "__main__":
	main();
