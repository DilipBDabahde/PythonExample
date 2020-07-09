#User Defined Functions

def Demo1():
	print("inside Demo1")
	#this fun accept nothing and return nothing


# Function which accepts value and return nothing
def Demo2(value):
	print("inside Demo2");
	print("Accepted value is: ",value);


# Function which accepts value and return value

def Demo3(value):
	print("Inside Demo3");
	print("Accepted value is: ",value);
	return value + 1;

# Function which accepts multiple values and return multiple values

def Demo4(val1, val2):
	print("Inside Demo4");
	
	add = val1 + val2;
	sub = val1 - val2;
	return add, sub;


#nested function call
def Demo5():
	print("Inside Demo5");
	Demo1();

# nested function definition
def Demo6():
	print("inside Demo6");
	def InnerFun():
		print("Inside InnerFun");
	InnerFun();

# Function calls for above functions

Demo1();
Demo2(32);
ret = Demo3(32);
print("Demo3 return :",ret);

r1, r2 = Demo4(55,55);
print("Addition is: ",r1);
print("Subtraction is: ",r2);

Demo5(); #nested calling

Demo6(); # nested function definition



 
