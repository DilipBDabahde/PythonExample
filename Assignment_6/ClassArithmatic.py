'''
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
'''

class Arithmatic:
	
	def __init__ (self):
			self.Value1 = 0;
			self.Value2 = 0;
	
	def Accept(self):
		self.Value1 = int(input("Enter val1: "));
		self.Value2 = int(input("Enter val2: "));
		

	def Addition(self):
		print("inside Addition");
		return self.Value1 +  self.Value2;
	
	
	def Subtraction(self):
		print("inside Subtract");
		if self.Value1 > self.Value2:
			return self.Value1 - self.Value2;
		else:
			return self.Value2 - self.Value1;
	
	def Multiplication(self):
		print("inside Multi");
		return self.Value1 * self.Value2;
	
	def Division(self):
		print("inside Division");
		return self.Value1 // self.Value2;
	

obj1 = Arithmatic();
obj1.Accept();
print(obj1.Addition());
print(obj1.Subtraction());
print(obj1.Multiplication());
print(obj1.Division());
