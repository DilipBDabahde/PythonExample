# calling to Helper_functions


from Helper_Functions import *

def main():
	
	rawdata = accept_data();
	print("Accepted list is: ",rawdata);
	
	filter_data = list(filter(chkEven, rawdata));
	print("Filter data is: ",filter_data);
	
	modified_data = list(map(modify, filter_data));
	print("Modified data is: ",modified_data);
	
	import functools
	result = functools.reduce(add, modified_data);
	print("Final output is: ",result);
	 	
	
if __name__ == "__main__":
	main();
