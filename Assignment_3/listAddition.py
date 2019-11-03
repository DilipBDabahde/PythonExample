'''
1).Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
'''

def List1():


	def Addition(list2): # named innser function use line 11 to 15  and called from line 27
		sum=0;
		for i in range(0,len(list2)):
			sum = sum + list2[i];
		return sum;
	
	arr = list();		#EMPTY LIST CREATED	
	num = input("Enter size of list: ");
	print("Enter values for list");
	
	for i in range(0,int(num)):
		no = input("Num: ");
		arr.append(int(no));
	
	print("Entered elements for list :",arr);
	
	result = Addition(arr);
	print("Addition of all elements is: ",result)
	return result
	
 

def main():
	icnt = List1();
	print("From main :",icnt);
	
if __name__ == '__main__':
		main();
