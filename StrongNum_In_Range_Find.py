''' 
accept range from user and display strong numbers from that range
input: 1 - 1000
output: 1 2 145


'''


def Dis_Strong_Nums_From_Range(Src, Dest):
	icnt=isum=digit=0;
	ifact = 1;
	
	while Src <= Dest:
		
		icnt = Src;
		while icnt != 0:
			digit = icnt % 10;
			while digit != 0:
				ifact = ifact * digit;
				digit = digit - 1;
			
			isum = isum +ifact;
			icnt = int(icnt/10);
			ifact = 1;
			
		if isum == Src:
			print(isum, end=' ');
		
		isum = 0;
		
		Src = Src + 1;

def main():
	isource = int(input("Enter source: "));
	idest= int(input("Enter destination: "));
	Dis_Strong_Nums_From_Range(isource,idest);
	print("")


if __name__ == '__main__':
	main();
	
