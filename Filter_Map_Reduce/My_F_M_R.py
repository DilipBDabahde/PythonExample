from functools import reduce 

def MyFilter(iNo):
	print("Hello from filter")
	if iNo >= 70 and iNo <= 90:
		return True;

def MyMap(iNo):
	print("Hello from map")
	return iNo+10;

def MyReduce(iNo1,iNo2):
	print("Hello from reduce")
	return iNo1+iNo2;
	
