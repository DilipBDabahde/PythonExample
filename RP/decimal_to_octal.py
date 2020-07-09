#wap which accept decimal value and convert it into octal



def octal(no):
	#base of octal is 8
	isum = 0;
	while no != 0:
		isum = isum * 10 + (no%8);
		no = no // 8;
	
	no = isum;
	isum = 0;
	while no != 0:
		isum = isum * 10 + no%10;
		no = no//10;
	return isum;


def main():
	
	ival = int(input("Enter number: "));
	res = octal(ival);
	
	print("octal of {} is {}".format(ival,res));


if __name__ == "__main__":
	main();

