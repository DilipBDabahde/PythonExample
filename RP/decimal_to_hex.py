#wap which accept number from user and convert decimal to hexdecimal and display on console


def hex(no):
	bit = 0;
	arr = ['A','B','C','D','E','F']
	arr_list =list();
	
	while( no != 0):
		bit = int(no%16);
		if bit <= 9:
			arr_list.append(bit)
		else:
			arr_list.append(arr[bit-10]);
		no = int(no/16);
	
	size = len(arr_list);
	size = size -1;
	while size >= 0:
		print(arr_list[size], end=" ");
		size = size - 1;
		
	

def main():
	
	ival = int(input("Enter number: "));
	
	hex(ival);
	print();

if __name__ == "__main__":
	main();
