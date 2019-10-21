# accept two nums and display comman factors of them
#input: 12 18
#output: 1 2 3 6 


def ComFactor(no1, no2):
	for i in range(1,no1):
		if no1%i == 0 and no2%i==0:
			print(i);
	
import sys;
def main():
	ival1 = int(sys.argv[1]);
	ival2 = int(sys.argv[2]);
	
	ComFactor(ival1, ival2);


if __name__ == '__main__':
	main();
