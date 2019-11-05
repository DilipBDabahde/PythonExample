'''
5.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

'''

from functools import reduce

def ChkPrime(iNo):
	icnt = 0;
	for i in range(2,iNo):		
			
		if iNo%i == 0:
			icnt = icnt + 1;
	
	if icnt > 0:
		return False;
	else:
		return True;
		
		
		
def Multi_Prime_Num(iNo):
	return iNo*2;
	

def Reduce_Sum(iNo1,iNo2):
	return iNo1+iNo2;
		

def Acceptdata():

	num = input("enter size of list: ");
	print("Enter values for list ");
	arr = list();
	
	for i in range(int(num)):
		arr.append(int(input("Num: ")));
	
	print("Our list is ",arr)
	
	return arr;
	
	
def main():
	arr = Acceptdata();
	
	
	prime_filter = list(filter(ChkPrime,arr));
	print("After filter out prime nums list is : ",prime_filter);
	
	prime_map = list(map(Multi_Prime_Num,prime_filter));
	print("After mapped list is :",prime_map);
	
	prime_reduce = reduce(Reduce_Sum,prime_map);
	print("Result is :", prime_reduce);
	



if __name__ == "__main__":
	main();
