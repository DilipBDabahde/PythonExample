'''
Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
input: Number if elements : 4
input Elements: 12 7 6 5
output: 5

'''


def min_Find(arr):
	if len(arr) < 0:
		print("invalid input");
		return 0;
	
	min = arr[0];
	
	for i in range(0,len(arr)):
		if  arr[i] < min:
			min = arr[i];
	
	return min;



def main():
	
	arr_list = list(); #created empty list
	size = input("Enter list size: ");
	size = int(size); # type conversion
	
	print("Enter elements for list");
	
	for i in range(0,size):
		no = input("Enter element:");
		no = int(no);
		arr_list.append(no);
		
	#created list above using loop
	
	print("List is ready now: ",arr_list);
	
	result = min_Find(arr_list);
	
	print("min num from  given list is: ",result);
	

if __name__ == "__main__":
	main();
	
