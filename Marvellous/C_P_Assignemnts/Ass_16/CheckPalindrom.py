'''
accept N Nums from user and display palindrom

input : N = 5
	   	44   25   34   999 65

output:  44  999
'''



def checkPalindrom(arr):

	itemp = ifact = 0;
	i = 0;
	j = len(arr)-1;
	brr = [];
	while i <= j:
		
		itemp = arr[i];
		
		while itemp != 0:
			ifact = ifact * 10 + itemp % 10;
			itemp = int(itemp/10);
	
		if ifact == arr[i]:
			brr.append(ifact);
		i = i + 1;
		ifact = 0;
	
	print("Total palindroms are: ",brr);
	

def main():

	size = int(input("Enter size: "));
	arr = [];
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	
	if size == len(arr):
		
		checkPalindrom(arr);
	else:
		print("Invalid input:");



if __name__ == "__main__":
	main();
