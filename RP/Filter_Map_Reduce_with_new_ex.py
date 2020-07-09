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

'''


def user_filter(no):
	if no >= 70 and no <= 90:
		return True;
	else:
		return False;


def user_map_add(no):
	return no + 10;


def user_reduce(no1, no2):
	return no1 * no2;


def main():
	
	arr_list = list(); # list class object is created
	
	size = int(input("Enter sizeof list:"));
	
	for i in range(0,size):
		no = int(input("Enter element: "));
		arr_list.append(no); # adding element to list
	
	#created list successfully
	print("Created list is: ",arr_list);
	
	filter_list = list(filter(user_filter, arr_list));  # filterize data 
	print("new filtered list of 70 to 90 :",filter_list);
	
	map_list = list(map(user_map_add, filter_list));  # each element value is increased by 10
	print("now each element is increased by 10 value: ",map_list);
	
	import functools
	output = functools.reduce(user_reduce, map_list);
	
	print("After reducing our final output is: ",output);


if __name__ == "__main__":
	main();
	

