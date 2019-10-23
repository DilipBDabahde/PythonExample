'''
2. Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11   Output : Odd Number
Input : 8    Output : Even Number
'''



def ChkNum(iNo):
	if iNo % 2 == 0:
		print("Number is Even");
	else:
		print("Number is Odd");
		
		

def main():
	ival = int(input("Enter a value :"));
	ChkNum(ival);
	

if __name__ == '__main__':
	main();
