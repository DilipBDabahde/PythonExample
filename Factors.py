#accept num from user and print factors of that numbers
#input: 15
#output: 1 3 5

#input: 21
#output: 1 3 7

def Factors(iNo):
		
	for i in range(1,iNo):
		if(iNo % i == 0):
			print(i,"",end="");
	print("");

import sys;
def main():

	val = int(sys.argv[1]);
	Factors(val);
	
	
if __name__ == "__main__":
	main();

