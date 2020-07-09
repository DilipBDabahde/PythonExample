#wap which accept decimal from user and display binary of that number

def bin(no):
	isum =0;
	arr = list();
	
	while no != 0:
		digit = no % 2;
		if digit == 0:
			arr.append(digit);
		elif digit == 1:
			arr.append(digit);			
		no = no // 2;
	
	size = len(arr)-1;
	
	while size >= 0:
		print(arr[size], end=" ");
		size = size - 1;
		

def main():
	
	ival = int(input("Enter number:"));
	print("Binary of {} ".format(ival));
	result = bin(ival);
	print();


if __name__ == "__main__":
	main();
