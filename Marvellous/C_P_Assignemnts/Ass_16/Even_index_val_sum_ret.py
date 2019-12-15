'''
accept N values from user for list and return summation of such number whose index and data is even

input: listsize = 5
		0   1   2   3   4
		5   6   8   2   2
				8       2 = 10

output: 10

'''

def evennum_index(arr):

	even = odd = i = 0;
	
	for i in range(len(arr)):
		if arr[i]%2==0 and i % 2 == 0:
			even = even + arr[i];
	
	return even;

def main():
	
	size = int(input("Enter list size:"));
	
	arr = []; # empty list
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	
	if size == len(arr):
		
		res = evennum_index(arr);
		print("Sum of even index & data is: "res);
	else:
		print("Invalid input:");


if __name__ == "__main__":
	main();
