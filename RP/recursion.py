# recursionn in


print("Demo of scopre of recursion");

import sys

print(format(sys.getrecursionlimit()));

#changing recursion limit

sys.setrecursionlimit(1500);

print("max num of recursive calls are",format(sys.getrecursionlimit()));

def fact(no):
	print(no);
	if no == 0:
		return 1;
		
	
	return 	no * fact(no - 1);
	


val = int(input("Enter num: "));
ret = fact(val);

print("Factorial of {} is {}".format(val, ret))

