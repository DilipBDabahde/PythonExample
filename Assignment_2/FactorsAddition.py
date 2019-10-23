"""
4.Write a program which accept one number form user and return addition of its factors.
Input :12
Output : 16 	(1+2+3+4+6)
"""



def Add_of_Factors(iNo):
	
	if iNo < 0:
		return -1;
	sum = 0;
	for i in range(1,iNo//2+1):
		if iNo % i == 0:
			sum += i;
	
	return sum;

def main():
	
	ival = int(input("Enter val: "));
	ival = Add_of_Factors(ival);
	
	if ival == -1:
		print("Invalid input");
	else:
		print("Addition of all Factors is : ",ival);

if __name__ == "__main__":
	main();
