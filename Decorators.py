
#sub function gets call from inner funtion because 
def sub(a,b):		#address of sub is 2000
	print(a-b);



# smartsub is fun which get input as another fun name
#outer function
def SmartSub(fpointer):   # fpointer holds address 2000 

	
	#inner function 
	def inner(a,b):  #address of inner is 1000
		if a < b:				# if a less than b then it swaps
			b,a = a,b;			
		#inner fuction calls our sub function and return
		return fpointer(a,b);  #from this line call goes to address 2000
	
	
	
	
	#this is return of outerfunction but return innner function address
	return inner;

#from below line we call SmartSub function we pass address of address of sub 
#Smart SmartSub return address of innner , that stored into sub
sub = SmartSub(sub);	# 2000 send to SmartSub and SmartSub Return 1000 address which stores into sub

#now we can call sub function which is our decorator function
print("Subtraction of 7 and 2 is:");
#from below line we derectly call to inner function
sub(7,2);	#we call to 1000 address where inner function is stored

