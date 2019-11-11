'''
accept range from user and print range in reverse 
input: 5 10
output: 10 9 8 7 6 5
'''



def Dis_Rev_Range(Src,Dest):
	
	while Dest > Src:
		print(Dest, end=" ");
		Dest -=1;


def main():
	
	val1 = int(input("Enter val:"));
	val2 = int(input("Enter val:"));
	Dis_Rev_Range(val1,val2);
	print();sss
	

if __name__ == '__main__':
	main();
