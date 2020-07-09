#Duck Typing example

print("Demonstration of Duck Typing")

class Sparrow:
	def fly(self):
		print("Sparrow flying");
		

class Airplane:	
	def fly(self): 
		print("Airplane flying");

class Whale: # whale is type of fish
	def swim(self):
		print("Whale swimming");

#type of entity is not specified
#we expect entity to have a callable named fly at run time


def fun(entity):
	entity.fly(); # entity is class obj


sparrow_obj = Sparrow();
airplane_obj = Airplane();
whale_obj = Whale();

# above three class objs are created

fun(sparrow_obj); # output: Sparrow flying

fun(airplane_obj); # output: Airplane flying

#fun(whale_obj); 
'''
if we pass whale class object to fun method then it shows be error type
its correct error bcs whale class doesnot contains this fly method and also whale is fish which stays in water so it does not look like birds and it does not have wings to fly.
AttributeError: 'Whale' object has no attribute 'fly' '''

