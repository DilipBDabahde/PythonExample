'''
2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
'''
	
ROI = 10.5;
	
class BankAccount:
	
	def __init__(self,naav,amt):
		print("inside init");
		self.Name =naav;  # input("Enter Name: ");
		self.Amount = amt; #float(input("Enter Amount: "));
		
	
	def Deposit(self,amt):
		print("After dpositing: ",amt);
		self.Amount =	self.Amount + amt; 
		
	def Withdraw(self,amt):	
		print("After withdrawing: ",amt);	
		self.Amount = self.Amount - amt;
	
	def CalculateInterest(self):
		global ROI;
		return int((self.Amount/100)*ROI);
		
	
	def Display(self):
		print("Name: ",self.Name);
		print("Amount: ",self.Amount);
	
		
		
		
		
obj1 = BankAccount("Amit",5000);
obj1.Display();
print("Calculate interest: ",obj1.CalculateInterest());
obj1.Deposit(300);
obj1.Display();
obj1.Withdraw(350);
obj1.Display();
print("Calculate interest: ",obj1.CalculateInterest());
