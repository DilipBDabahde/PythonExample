'''
We can also convert the above Numbering system conversion program using recursion.
'''

arr_list = list();

def Binary(no):
	global arr_list
	if no != 0:
		bit = int(no%2);
		arr_list.append(bit);
		no = int(no/2);
		Binary(no);

arr_list1 = [];
def Octal(no):
	global arr_list1
	if no != 0:
		bit = int(no%8);
		arr_list1.append(bit);
		no = int(no/8);
		Octal(no);


arr_list2 = list()
def Hexadecimal(no):
	arr = ['A','B','C','D','E','F'];
	global arr_list2
	if no != 0:
		bit = int(no%16);
		if bit <= 9:
			arr_list2.append(bit);
		else:
			arr_list2.append(arr[bit-10]);
		no = int(no/16);
		Hexadecimal(no);


def main():
	value = int(input("Enter no: "));
	print("Value in Decimal format", value);
	print("------------------------------------");
	
	print("Value in Binary format");
	Binary(value);
	size = len(arr_list)-1;
	while size >= 0:
		print(arr_list[size],end="");
		size = size - 1;		
	print("\n------------------------------------");

	
	print("Value in Octal format")
	Octal(value);
	size = len(arr_list1)-1;
	while size >= 0:
		print(arr_list1[size],end="");
		size = size - 1;		
	print("\n------------------------------------");
	
	
	
	print("Value in Hexadecimal format");
	Hexadecimal(value);
	size = len(arr_list2)-1;
	while size >= 0:
		print(arr_list2[size],end="");
		size = size - 1;		
	print("\n------------------------------------");


if __name__ == "__main__":
	main();
	
	
		

