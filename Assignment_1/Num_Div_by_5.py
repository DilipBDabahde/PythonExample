"""
7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8
Output : False

Input : 25
Output : True

"""



def Fun(iNo):
	if iNo % 5 == 0:
		return True;
	else:
		return False;

def main():

	ival = int(input("Enter a val: "));
	Res = Fun(ival);
	if Res == True:
		print("Given num is div by 5");
	else:
		print("Given num is not div by 5");
		
	
if __name__ == "__main__":
	main();
