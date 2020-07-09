'''
Write a program which contains one function named as ChkNum() which accept one 
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.

Input: 11	Output: OddNum
Input: 14	Output: EvenNum

'''

def check_num(no):

	if no % 2 == 0:
		print("EvenNum");
	else:
		print("OddNum");


def main():
	
	ival = int(input("Enter a Num: "));
	check_num(ival);


if __name__ == "__main__":
	main();
	


