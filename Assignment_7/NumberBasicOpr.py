'''
3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.
'''




class Arithmatic:
	
	def __init__(self,val):
		self.no=val;
	
	def ChkPrime(self):
		ival = 0;
		for i in range(2,self.no+1):
			if self.no % i == 0:
				ival = ival + 1;
			
		if ival==1:
			return True;
		else:
			return False;


	def ChkPerfect(self):
		sum = 0;  # perfect num is such num which is addition of its all factors
		
		for i in range(1,self.no):
			if self.no % i == 0:
				sum = sum + i;
		if sum == self.no:
			return True;
		else:
			return False;	
	
	
	def SumFactors(self):
		sum = 0;
		for i in range(1,self.no+1):
			if self.no % i == 0:
				#print(i);
				sum += i;	
		return sum;
	
		
	def Factors(self):
		print("All Factoris of given num is: ",end="");
		for i in range(1,self.no+1):
			if self.no % i == 0:
				print(i, end=" ");


val = int(input("Enter a val:"));

aobj = Arithmatic(val);


res = aobj.ChkPrime();	
if res == True:
	print("Given num is Prime: ",val);
else:
	print("Given Num is not Prime: ",val);

res = aobj.ChkPerfect();
if res == True:
	print("Given num is Perfect: ",val);
else:
	print("Given Num is not Perfect: ",val);
	
res = aobj.SumFactors();
print("Sum of all factoris is: ",res);

aobj.Factors();
print();


