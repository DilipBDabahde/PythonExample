'''
accept range from user and return addition of them
input: 5 10
output: 5+6+7+8+9+10 = 45
'''



def RangeSum(Src, Dest):
	sum = 0;
	for i in range(Src,Dest+1):
		sum += i;
	
	return sum;		
	


def main():
	val1 = int(input("Enter a val: "));
	val2 = int(input("Enter a val: "));
	res =RangeSum(val1,val2);
	print("Sum of all range members is: ",res);



if __name__ == '__main__':
	main();
