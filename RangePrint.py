'''
ACCEPT range START AND END VAL FROM USER AND PRINT NUMS FROM THAT RANGE AND END SHOULD BE GREATER THAT START
INPUT: 51 66
OUTPUT: 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
'''





def Dis_RangeVal(Src, Dest):

	for i in range(Src,Dest):
		print(i,end=' ');


def main():
	
	suru = int(input("Enter source:"));
	shevat = int(input("Enter dest:"));
	
	Dis_RangeVal(suru,shevat);
	print();
	

if __name__ == '__main__':
  main();
