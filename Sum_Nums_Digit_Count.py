'''
Write a program which accept 5 numbers from user and print addition of digits of each number.
input: 7 57 7546  456 24
output:7 12 22 	  15  6  
'''


def AdditionOfDigit(ilist):
	sum = 0;
	digit = 0;
	MILIST=[];
	icnt =0;
	i=0;
		
	while(i < len(ilist)):
		digit = ilist[i];
		sum=0;
			
		while( digit != 0):
			icnt = digit%10;
			sum = sum + icnt;
			digit = int(digit/10);
		MILIST.append(sum);
		i = i + 1;
	
	print("Our list is: ",ilist);
	print("Our list Nums digit sum: ",MILIST);
	
	
def main():
	
	list_A = [];
	size = 5;
	print("Enter 5 numbers");
	for i in range(size):
		list_A.append(int(input("Enter num: ")));
	AdditionOfDigit(list_A);
	
if __name__ == '__main__':
	main();
