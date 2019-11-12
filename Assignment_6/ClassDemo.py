'''
1.Write a program which contains one class named as Demo.
Demo class contains two instance variables as no1 ,no2.
That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance
variables.
Initialise instance variable in init method by accepting the values from user.

After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
'''


class Demo:
	Value = 0;
	
	def __init__(self,val1, val2):
		self.no1= val1;
		self.no2= val2;
		
	def Fun(self):
		print("from fun");
		print(self.no1);
		print(self.no2);
	
	def Gun(self):
		print("from gun");
		print(self.no1);
		print(self.no2);
	


def main():

	obj1 = Demo(11,21);
	obj2 = Demo(51,101);


	obj1.Fun();
	obj2.Fun();
	obj1.Gun();	
	obj2.Gun();

if __name__ == '__main__':
	main();



