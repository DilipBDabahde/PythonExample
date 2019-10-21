"""
 accept one num from user and make addition of even num till given val
 input: 13
 	2+4+6+8+10+12	Even
 output:42
 
 
 input: 7
 	2+3+6
 output:11
 
 """

def EvenSum(no):
	sum = 0;
	for i in range(1,no):
		if (i % 2 == 0):
			sum+=i;	
	return sum;
	
import sys;
def main():
	
	iNo = int(sys.argv[1]);
	iNo1 = EvenSum(iNo);
	
	print('Sum of Even is : ',iNo1);
	

if __name__ == '__main__': 
	main();
