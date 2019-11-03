'''
5.Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from 
that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our
user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)

'''



def CheckPrime(iNo):
		
		icnt=ival=0;
		
		for i in range(2,iNo):			
			if i > iNo//2:
				break;				
			if iNo%i==0:
				icnt += 1;
		
		if icnt == 0:
			return True;
		else:
			return False;


def PrimeAddition(Listx):
	
	sum = 0;
	my_arr=list();
	for i in range(0,len(Listx)):
		res = CheckPrime(Listx[i]);
		if res == True:
			my_arr.append(Listx[i]);
			sum +=Listx[i];

	print(my_arr);
	print("Sum of Prime Nums is: ",sum)
	


def main():

	arr = list();
	num = input("Enter list size: ");
	print("enter values for list");
	
	for i in range(0,int(num)):
		no = input("Num:["+str(int(i+1))+"]:");
		arr.append(int(no));
		
	print(arr);
	
	PrimeAddition(arr); # fuc call


if __name__ == "__main__":
	main();

