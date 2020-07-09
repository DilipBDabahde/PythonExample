'''
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.

we have to create moduel with four behaviour add(), sub(), mult(), div()

'''


def Add(no1, no2):
	ans = no1 + no2;
	return ans;


def Sub(no1, no2):
	ans = 0;
	
	if no1 > no2:
		ans = no1 - no2;
	else:
		ans = no2 - no1	
	return ans;
	

def Mult(no1, no2):
	ans = 0;
	if no1 > 0 and no2 > 0:
		ans = no1 * no2;	
	return ans;
	
	
def Div(no1, no2):
	ans = 0;
	ans = no1 // no2;
	return ans;
	
