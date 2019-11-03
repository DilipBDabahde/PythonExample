'''
2).Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 37
Output : 56
'''

def Find():
	
	def Max(listx): #named inner function
		max_ = 0;
		
		for i in range(0,len(listx)):
			if max_ < listx[i]:
				max_ = listx[i];
		
		return max_;
	
	arr = list(); #empyt list created
	num = input("Enter size of list: ");
	print("Enter values");
	
	for i in range(0,int(num)):
		no = input("Num :");
		arr.append(int(no));
	
	print("Entered elements are :", arr);
	
	result = Max(arr);
	print("Max Val is : ",result);

def main():
	Find();



if __name__ == "__main__":
	main();
