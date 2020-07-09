'''
Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input : Number of elements : 4
input Elements: 12 5  6 7
output: 12

'''



def maxFind(arr):
	max = 0;
	
	for i in range(0,len(arr)):
		if arr[i] > max:
			max = arr[i];
	
	return max;


def main():
	
	arr = list();
	size = input("Enter size: ");
	size = int(size); # type conversion
	
	for i in range(0,size):
		no = input("Enter element: ");
		no = int(no);
		arr.append(no);
	
	result = maxFind(arr);
	print("created list is: ",arr);
	
	print("Max num from given list is: ",result);

if __name__ == "__main__":
	main();

	
