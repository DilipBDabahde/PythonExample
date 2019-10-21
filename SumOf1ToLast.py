'''
accept num from user and display its addition till last num
input: 7
output: 1+2+3+4+5+6+7 = 28
input:3
output: 1+2+3= 6
'''

def NumAdd(iNo):
	sum = 0;
	for i in range(0,iNo+1):
		sum = sum + i;
	
	return sum;
	

def main():
	
	val = int(input("Enter a val: "));
	total = NumAdd(val);
	print("Sum of all nums from 1 to given num is: ",total);
	

if __name__ == "__main__":
	main();
