'''
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

implementing lambda

'''

def main():
	
	arr_list = list(); # list class object is created
	
	size = int(input("Enter sizeof list:"));
	
	for i in range(0,size):
		no = int(input("Enter element: "));
		arr_list.append(no); # adding element to list
	
	#created list successfully
	print("Created list is: ",arr_list);
	
	filter_list = list(filter(lambda no : (no >= 70 and no <= 90),arr_list));
	print("Filter list is: ",filter_list);
	
	map_list = list(map(lambda no : no + 10, filter_list));
	print("Map list is: ", map_list);
	
	import functools
	result = functools.reduce(lambda a,b : a * b, map_list);
	
	print("Final output is :", result);


if __name__ == "__main__":
	main();


