
print("Demonstration of Behaviours of Class")


class Demo:

	def __init__(self):	 # this is like constructor to allocate resources
		
		self.i = int(input("Enter value first: "));
		self.j = int(input("Enter value second: "));
	
	def fun(self): 
		print("inside instance method",self.i + self.j);
	
	
	@classmethod # decorator
	def gun(cls): # cls is req argument
		
		print("inside  class method");
	
	
	@staticmethod	#decorator
	def sun():
		print("inside static");
	

obj1 = Demo(); #class obj created

obj1.fun();
Demo.gun();
Demo.sun();

