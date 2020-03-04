
def hexx(ino):
	arr = ['a','b','c','d','e','f']
	bit = 0;
	
	if(ino != 0):
		bit = int(ino%16)
		if(bit <= 9):
			print(bit,end="");
		else:
			print(arr[bit-10],end="");
		
		ino = int(ino/16);
		hexx(ino);
	print();

val = int(input("Enter value  to see its hex num: :"));

hexx(val);
