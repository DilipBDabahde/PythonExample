#Accept Num from user and check it's palindrome or not

#input: 675
#output: it's not palindrom

#input: 676
#output: its palindrom

def ChkPalindrome(iNo):

	Modify = 0;
	Temp = iNo;
	
	while iNo > 0:
		digit = iNo % 10;
		Modify = 10 * Modify + digit;
		iNo /= 10;
	
	if Temp == Modify :
		return True;
	else:
		return False;


def main():
	
	icnt = input("Enter a Num: ");
	
	res = ChkPalindrome(int(icnt));
	
	if res == True:
		print("Given Num is Palindrome");
	else:
		print("Given num is not palindrome");



if __name__ == "__main__":
	main();
