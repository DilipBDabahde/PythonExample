# serial processing approach
from time import *

def square(n):
	return n*n;


def main():

	#input list
	arr = [1,2,3,4,5];
	#empty list to store result
	result=[]
	
	starttime=time();
	for num in arr:
		result.append(square(num));
	endtime=time();
	print(endtime-starttime);
	print(result);
	

if __name__ =="__main__":
	main();
