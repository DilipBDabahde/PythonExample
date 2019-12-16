'''
accept list from user and replace each element if element is even then replace with 0 for odd is 1
'''

def EvenOddReplacement(arr):
	
	print(arr);
	for i in range(len(arr)):
		if arr[i]% 2 == 0:
			arr[i]= 0;
		else:
			arr[i] = 1;	
	print(arr);

def main():
	
	size = int(input("Enter size: "))
	arr = [];
	for i in range(size):
		arr.append(int(input("Enter num: ")));

	EvenOddReplacement(arr);		

if __name__ == "__main__":
	main();
