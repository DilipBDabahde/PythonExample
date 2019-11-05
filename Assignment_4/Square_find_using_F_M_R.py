'''
4.Write a program which contains filter(), map() and reduce() in it. Python application whichontains one list of 
numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are
even. Map function will calculate its square. Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204

'''

from functools import reduce



def Acceptlist():

	size = input("enter size of list: ");
	print("Enter vlaues for list");
	arr = list();
	
	for i in range(int(size)):		#typecasted
		no = input("Num :");
		arr.append(int(no));	 	# appending values in list
	
	print("Our list is---> ",arr);
	return arr;




def main():

	arr = Acceptlist();
	
	#using Lambda function for above give task
	
	list_filter = list(filter(lambda no : (no%2==0),arr));  # filtering our even and storing in list_filter
	print("After filter out even list is: ",list_filter);
	
	#now processing for square 
	
	list_map = list(map(lambda no: (no*no),list_filter));  #mapped data
	print("square of even values is: ",list_map);
	
	list_reduce = reduce(lambda no1,no2: (no1+no2),list_map);
	print("Final result is : ",list_reduce);



if __name__ == "__main__":
	main();
