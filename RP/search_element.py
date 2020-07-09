'''
.Write a program which accept N numbers from user and store it into List. Accept one another number from user and
return frequency of that number from List.

input: Num of elements: 12
input Elements: 5  8  6  8  5  9  3  7  2  21  1  5
Element to search = 5
output: Freq of search element is: 3
'''



def search_Element(arr, iNo):
	
	if len(arr) < 0:
		return -1;
	
	icnt = 0;	# icnt is counter variable which is used to increament it's value by One when we get our Element
	
	for i in range(0, len(arr)):
		if arr[i] == iNo:
			icnt = icnt + 1;		
	
	return icnt;


def main():
	
	arr_list = list();  # arr_list is object of list class , this object is used to add elements in it
	
	size = input("Enter list size: ");
	
	size = int(size);  # type conversion of size variable str to int
	
	print("Enter elements for list");
	
	for i in range(0, size):
		no = input("Enter element: ");
		no = int(no);	# type conversion
		arr_list.append(no);  # appending element to list class object
	
	#now our list is created using loop iteration
	
	print("Created list is: ",arr_list);
	
	
	search_var = input("Enter number to search its freq:");
	search_var = int(search_var);
		
	result =search_Element(arr_list, search_var);
	
	if result > 0 :
		print("FReq of given variable in list is: ",result);
	elif result == 0:
		print("There is no element in list ");
	else:
		print("Invalid input");

if __name__ == "__main__":
	main();

	
	
	
