'''
accept list from user and display 	power of each number where base values is list element and find power as per base value index


input:	
	  index---> 0  1  2  3  4
	  lixt ---> 6  7  8  3  4
	  output:   1  7  64 27 256
'''


def displayPower(arr):

	brr = [];	
	print("Our list is:",arr);
	j = isum = itemp = 0;
	for i in range(len(arr)):
		
		itemp = arr[i];
		j = i;
		
		if j == 0:
			brr.append(1);
			
		else:		
			isum = 1;	
			while j != 0:				
				isum = isum * itemp;
				j = j - 1;
				
			brr.append(isum);
			
	print("List with power valuse: ",brr);



def main():
	
	size = int(input("Enter list size:"));
	
	arr = []; #empty list
	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	
	if size == len(arr):
		displayPower(arr);
	else:
		print("invalid input");




if __name__ == "__main__":
	main(); 
