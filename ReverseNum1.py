#accept num from user and return it's reverse num
#input : 6548
#output: 8456
# use cmd to run : python filename 


def ReverseNum(iNo):
	Modify = 0;
	
	while iNo > 0:
		digit = iNo % 10;
		Modify = 10 * Modify + digit;
		iNo /= 10;
	
	return Modify;

def main():

	val = input("Enter Num: ");
	res = ReverseNum(int(val)); #typecast
	print("Reverse of Given num is: ",res);


if __name__ == '__main__':
	main();

