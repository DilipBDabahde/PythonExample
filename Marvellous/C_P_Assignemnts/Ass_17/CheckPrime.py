'''
accept list from user and display all prime numbers from that list

input: 6
	  
	   5   67  90  13   64  23
	   5   67      13  		23	

'''

def CheckPrime(arr):
	j = 0
	for i in range(len(arr)):
		j = 2;
		while j <= arr[i]/2:
			if arr[i]%j == 0:
				break;
			j = j + 1
				
		if j > arr[i]/2:
			print(arr[i])		
		
def main():
	
	size = int(input("Enter number from user.."));
	arr = [];
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	CheckPrime(arr);


if __name__ == "__main__":
	main();
