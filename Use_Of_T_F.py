'''
accept one num and check it is div by 5 or not 

input: 23 
output: FALSE Not div
input:45
output: TRUE Div by 5
input: 66
output: FALSE Not Div


'''

import sys;

def CheckDiv(no):
	print("inside check")
	if no % 5 == 0:
		return True;
	else:
		return False;


def main():
	print("inside main");
	
	ival=int(sys.argv[1]);
	ires = CheckDiv(ival);
	
	if ires == True:
		print("Given num is div by 5");
	else:
		print("Given num is not div by 5")
		

if __name__ == '__main__':
	main();
