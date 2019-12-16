'''
accept list from user and one number display such elements which are divisible by number

input : list  5   6   8     7   9   20
	    num   2
	    
output:		  6   8   20
'''

def CheckDivisible(arr, num):
	print("Divisible By ",num);
	
	for i in range(len(arr)):
		if arr[i] % num == 0:
			print(arr[i]);
			
def main():
	
	size  = int(input("Enter size: "));
	arr = [];
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	print("Enter number for check divisible: ");
	num = int(input("Enter Number: "));
	
	CheckDivisible(arr, num);

if __name__ == "__main__":
	main();
	
