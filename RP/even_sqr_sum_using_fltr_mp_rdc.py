'''
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''


	
def evenNum(iNo):
	if iNo % 2 == 0:
		return True;
	else:
		return False;
			
	
def evenSquare(iNo):
	return iNo*iNo;
	
	
def evenSquareSum(a, b):
	return a+b;
	


def main():
	
	arr_list = list(); # created empty list  with object name arr_list
	
	size = int(input("Enter list size: "));
	
	print("Enter elements for list: ");
	
	for i in range(0,size):
		no = int(input("Enter element:"));
		arr_list.append(no);
	
	
	if len(arr_list) > 0:
		print("List is created successfully");
		even_list = list(filter(evenNum,arr_list));
		print("Even list is: ", even_list);
		
		even_sqr = list(map(evenSquare, even_list));
		print("Square of even numbs: ",even_sqr);
		
		import functools
		reduce_sqr_sum = functools.reduce(evenSquareSum, even_sqr);
		
		print("Sum of all even square is: ",reduce_sqr_sum);
	else:
		print("list is not created");

if __name__ == "__main__":
	main();

