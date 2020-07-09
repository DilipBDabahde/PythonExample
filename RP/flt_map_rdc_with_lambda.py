#Filter Map Reduce using Lambda Functions

from functools import *


def acceptData():
	size = int(input("Enter num of elements size:"));
	arr = list(); #created empty list
	print("Enter elements for list:");
	for i in range(0,size):
		no = input("Enter element: ");
		no = int(no); # type conversion
		arr.append(no); #addding to list
		
	return arr;
	
def main():
	
	rawdata = acceptData();
	print("Accepted list:",rawdata);
	
	filter_data = list(filter(lambda no : (not(no%2)),rawdata));
	
	print("Filtered data is: ",filter_data);
	
	modified_list = list(map(lambda no : no + 2, filter_data));
	print("Modified_list :",modified_list);
	
	if len(modified_list) > 0:
		output = reduce(lambda a, b : a + b, modified_list);
		print("Final output is: ",output);
	else:
		print("there is no result");
	
	
if __name__ == "__main__":
	main();
	
