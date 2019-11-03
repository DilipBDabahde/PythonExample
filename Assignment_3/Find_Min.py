'''
3).Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
'''

def Find():
	
	def Min(listx):
		min=listx[0];
	
		for i in range(0,len(listx)):
			if min > arr[i]:
				min = arr[i];
		return min;
	
	arr = list(); #empty list created
	num = input("Enter size of list: ");
	print("Enter values for list");
	
	for i in range(0,int(num)):
		no = input("Num:["+str((i+1))+"]: ");
		arr.append(int(no));
	
	print("Entered values are: ",arr);
	
	result = Min(arr);
	print("Min element is :",result);



def main():
	Find();
	
if __name__ == '__main__':
	main();
