'''
accept Num from user and check that num is armstrong or not
input: 153 
output: True
input: 166
output: False

the calculation of armstrong num is like
ex 153 this num contains 3 digits so from this num take each digit seperately and find power of that digit then make sum of all digits power and compare it with our first num if both are same then Print True else print False
  3 
 1 = 1*1*1   	 =1
 
  3
 5 = 5*5*5		 =125
 
  3
 3 = 3*3*3       =27
 						=125+27+1
 						=153		 True
'''

def CheckArmStrong(iNo):
	icnt =0;
	idigit = 0;
	isum = 0;
	ifact = 0;
	itemp=iNo;
	
	while iNo != 0:
		icnt = icnt + 1;
		iNo = int(iNo/10);
		
	iNo = itemp;	
	while(iNo != 0):
		
		idigit = icnt;
		ifact = 1;
		
		while(idigit != 0):
			ifact = ifact * (iNo%10);
			idigit = idigit - 1;
		isum = isum + ifact;
		iNo = int(iNo/10);
	
	if isum == itemp:
		print("Given Number is Armstrong: ",isum);
	else:
		print("Given Number is-Not Armstrong: ",isum);
	


def main():
	val = int(input("Enter a val:"));
	CheckArmStrong(val);


if __name__ == "__main__":
	main();
	
