
print("Demo of class");

class Demo:
	def __init__(self, val1, val2):
		print("inside init method");
		self.i = val1;
		self.j = val2;
	
	def fun(self):
		print("inside fun");
		print(self.i, self.j);
	
	def add(self):
		print(self.i + self.j);
	
#creating demo class object
#obj wise calling method

obj1 = Demo(11,21);
obj1.fun();
obj1.add();

#creating obj new
obj2 = Demo(50, 60);
obj2.fun();
obj2.add();

