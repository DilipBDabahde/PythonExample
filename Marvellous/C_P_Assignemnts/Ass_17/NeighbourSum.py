'''
accept integers list from user and check numbers neighbours sum is number

input: 6  7  8  1  14  2  6  4
	      |-----|      |-----|
	      	 +			  +
	      	 8  		  6     <------ output
'''


def DisplayNeighbourSum(arr):

	icnt = 0;
	isum = 0;
	i = 1;
	while i<= len(arr)-2:		
		if arr[i-1] + arr[i+1] == arr[i]:
			print(arr[i-1]," + ",arr[i+1]," = ",arr[i]);
		i = i + 1;

def main():
	
	size = int(input("Enter list size: "));
	
	arr = [];
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	DisplayNeighbourSum(arr);

if __name__ == "__main__":
	main()      	 
