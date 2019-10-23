#accept num from user and print its Collatz sequence
# input:3 
#output:10 5 16 8 4 2 1 


def Collatz(iNo):
	if iNo % 2 == 0:
		return iNo // 2;
	else:
		return 3 * iNo + 1;
	

def main():
	
	ival = int(input("Enter a val: "));
	
	while ival >= 1:
		if ival == 1:
			break;
		print(ival);
		ival = Collatz(ival);
		

if __name__ == "__main__":
	main();
