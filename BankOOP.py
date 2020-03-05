#bank processes implementation using Python



class Bank:
	
	ROI = 10.5;
	
	def __init__(self, AcNum, CustName, Amount):
		self.name = CustName;
		self.amount = Amount;
		self.AcNum =AcNum;
	
	def checkBal(self):
		print("your Account balance is: ",self.amount);
	
	def deposit(self,amount):
		self.amount += amount;
		print("your amount is successfully deposited:",amount);
	
	
	def withdraw(self,amount):
		if amount > self.amount:
			print("Insufficient balance");
		else:
			self.amount = self.amount - amount;
			print("Successfully withdrawn: ",amount);
			print("your currant balance is: ",self.amount);
	
	@classmethod
	def displayROI(cls):
		print("Roi is:",ROI);
	
	
	@staticmethod
	def bankInfo():
		print("Its National Bank")
		print("Location is pune");
		
	
	def custInfo(self):
		print("Customer Name: ",self.name);
		print("Customer Id: ",self.AcNum);



def main():
	print("inside main:");
	
	obj1 = Bank(1209,'Anil',5000);
	obj1.custInfo();
	obj1.checkBal();
	obj1.withdraw(5000);
	obj1.deposit(4000);
	obj1.checkBal();



if __name__ == "__main__":
	main();
