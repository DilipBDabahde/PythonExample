'''
accept range  from user and print even_nums from that range 
input: 51 66
output: 52 54 56 58 60 62 64 66
'''


def EvenFromRange(Src, Dest):
	
	if Src > Dest:
		print("invalid input sequence")
		return;
		
	for i in range(Src, Dest+1):
		if i % 2 == 0:
			print(i,end=' ');
			


def main():
	
	src = int(input("Enter val: "));
	dest = int(input("Enter val: "));
	
	EvenFromRange(src,dest);
	print();


if __name__ == '__main__':
	main();
