# from this file we are calling Arithmatic Module which has four function def as Add(),Sub(),Multi(),Div()

import Arithmatic;

def main():

	ival1 = int(input("Enter first Val: "));
	ival2 = int(input("Enter second val: "));
	
	Res = Arithmatic.Add(ival1, ival2);
	print("Result of addition is: ",Res);
	
	
	Res = Arithmatic.Sub(ival1, ival2);
	print("Result of Subtraction is: ",Res);
	
	
	Res = Arithmatic.Multi(ival1, ival2);
	print("Result of Multiplication is: ",Res);
	
	
	Res = Arithmatic.Div(ival1, ival2);
	print("Result of Division is: ",Res);
	

if __name__ == "__main__":
	main();
