'''
Write a program which accept 8 numbers from user and print number of digits of each number.
input: 7 45 2991 31 91 28711 9 90
output:1 2  4    2  2  5     1 2
'''

def Dis_Num_Of_Digit_From_Num(ilist):
	list2=[]
	for i in range(len(ilist)):
		iNo=ilist[i];
		icnt = 0;
		while iNo != 0:
			icnt = icnt + 1;
			iNo = int(iNo/10);
		list2.append(icnt);
	
	print(ilist);
	print(list2);


def main():
	list_A=[];
	size = int(input("Enter size of list: "));
	for i in range(size):
		list_A.append(int(input("Enter num: ")));
	
	Dis_Num_Of_Digit_From_Num(list_A);


if __name__ == '__main__':
	main();
