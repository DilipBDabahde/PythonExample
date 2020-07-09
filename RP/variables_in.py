#class variables in

print("Demo of characteristics of class")

class Demo:
	x = 10; #class variable
	
	def __init__(self, no1, no2):
		self.i = no1;
		self.j = no2; #this method like constru
	
	def add(self):
		print("Sum of values:",self.i + self.j);

obj1 = Demo(10,20);
obj1.add();

obj2 = Demo(11,22);

obj2.add();



'''
for instance variable value of instance variable change for each object

but in case of class variable its comman
it does not req object to use it outside the class

'''



