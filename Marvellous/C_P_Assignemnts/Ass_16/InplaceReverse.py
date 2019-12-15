'''
accept integer list from user and replace list values in place

input:  6
	  : 5   9   6   7  5  6
	  
output: 6   5   7   6  9  5

'''


def inPlaceReverse(arr):
	
	icnt = ival = 0;
	
	i = 0;
	j = len(arr)-1;
	print("Before change: ",arr);
	
	while i <= j:
		
		temp = arr[i];
		arr[i]= arr[j];
		arr[j]=temp;
		i = i + 1;
		j = j - 1;
	
	print("After change: ",arr);



def main():
	
	size  = int(input("Enter size:"));
	arr = [] # empty list
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	if size == len(arr):
		
		inPlaceReverse(arr);
	else:
		print("Invalid input:");



if __name__ == "__main__":
	main();
