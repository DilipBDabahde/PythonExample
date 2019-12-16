'''
accept integer list from user and if and element is divisible by 3 then increase it by 1 or if 	element is divisible by 3 and 5 then increase that element by 2
else keep as it is

input:	5
		12  3  54  65  15
		13  4  54  65    17
		
'''

def DisplayValue(arr):
	
	icnt = 0
	print(arr);
	for i in range(len(arr)):
		
		if arr[i] % 3 == 0 and arr[i] % 5 == 0:
			arr[i]= arr[i]+2;
		elif arr[i] % 3 == 0 :
			arr[i] = arr[i]+1;
		else:
			pass
	
	print(arr);


def main():
	
	size  =  int(input("Enter list size: "));
	
	arr = [];
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
		
	DisplayValue(arr);



if __name__ == "__main__":
	main();
