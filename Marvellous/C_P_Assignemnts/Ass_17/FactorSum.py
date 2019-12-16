'''
accept list from user and display additon of each elements factors

input: N   4
		   6       7   8    	9
		   
		   1+2+3   1   1+2+4  	1+3
		   6       1   7  		4
'''

def FactorSum(arr):
	brr=[];
	j = isum = 0;
	print(arr);
	
	for i in range(len(arr)):		
		j = 1;
		while j <=arr[i]/2:
			if arr[i] % j == 0:
				isum = isum + j;
			j = j + 1;
		brr.append(isum);
		isum = 0;
	
	print(brr);
			
		
		

def main():
	
	size = int(int(input("Enter size of list")));
	arr = [];
	for i in range(size):
		arr.append(int(input("Enter num: ")));
		
	
	FactorSum(arr);

if __name__ == "__main__":
	main();
