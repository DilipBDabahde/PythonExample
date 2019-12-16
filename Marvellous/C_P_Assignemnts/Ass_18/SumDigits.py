'''
acccept list from user display summation of each numbers digits

input:  45  66  2434   5846  24  53 
	    9   12  13     23    6   8   <---- output:
'''

from __future__ import print_function



def DigitSum(arr):
	
	if len(arr) <= 0:
		print("invalid input");
		exit();
		
	idigit = 0
	
	for i in arr:		
		while i != 0:
			idigit = idigit + i % 10;
			i = int(i/10);
		print(idigit,end=" ");
		idigit = 0;
		

def main():
	size  = int(input("Enter list size: "));
	arr = [];	
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	DigitSum(arr);

if __name__ == "__main__":
	main();
