'''
4).Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
'''

def Freq(listx, x):
		
		icnt = 0;
		
		for i in range(0,len(listx)):
			if listx[i] == x:
				icnt += 1;
		return icnt;		
		
		
def CheckFreq():		
		
	arr = list();
	num = input("Enter size of list: ");
	print("Enter vales for list");
	
	for i in range(0,int(num)):
		no = input("Num:["+str(int(i+1))+"]:");
		arr.append(int(no));
	
	
	no = input("Enter a val to check its frequency: ");
	
	print("Entered list is: ",arr);
	
	result = Freq(arr,int(no));# calling 
	print("Freq of given num is :",result)
    

def main():
	CheckFreq();


if __name__ == "__main__":
	main();
	
