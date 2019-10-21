'''
accept two nums from user through command line argv and return their addition
input: 11 33
output: 44

input: 4 5
output: 9
'''


def TwoNumAdd(no1, no2):
	Sum = no1 + no2;
	return Sum;


import sys;	
def main():
	
	iNo1 = int(sys.argv[1]);  # first command line argument req
	iNo2 = int(sys.argv[2]);  #second command line argument req
	
	result = TwoNumAdd(iNo1, iNo2);
	print("Add of two num is : ",result);
	

if __name__ == '__main__':
	main();
