'''
accept integers list from user and find even and odd do seperate even and odd return sum diff from even odd

input: size = 6
	   values ---->  7   5   6   2   4  9
	   even = 6+2+4 =12
	   odd  = 7+5+9 =21
	   
	   return 21 - 12

output: 09
'''


def EvenOddDiff(arr):
	
	even = odd = 0;
	
	for icnt in arr:
		if icnt % 2 == 0:
			even += icnt;
		else:
			odd += icnt;
	
	
	if even > odd:
		return even - odd;
	else:
		return odd - even;


def main():
	
	size = int(input("Enter list size:"));
	arr = []; #empty list created
	for i in range(size):
		arr.append(int(input("Enter num: ")));
	
	if size == len(arr):
		
		res = EvenOddDiff(arr);
		print("Even odd diff is: ",res);
	else:
		print("Invalid input:\n");




if __name__ == "__main__":
	main();
