"""
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"

"""



def Add(iNo1, iNo2):
	Ans = iNo1 + iNo2;
	return Ans;
	


def Sub(iNo1, iNo2):
	Ans = 0;
	
	if iNo1 > iNo2:
		return iNo1 - iNo2;
	else:
		return iNo2 - iNo1;



def Multi(iNo1, iNo2):
	
	if iNo1 < 0 or iNo2 < 0:
		return -1;	
	Ans = iNo1 * iNo2;
	return Ans;

def Div(iNo1, iNo2):

	if iNo1 < 0 or iNo2 < 0:
		return -1;
	
	Ans  = iNo1 // iNo2;
	return Ans;
	
