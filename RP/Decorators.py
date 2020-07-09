#decorator usage with demo

print("Demo of Decorators");

#subtraction of two nums

###################################################################

def sub(a,b):  #address temp 1000
	return a - b;
	
###################################################################

#smartSub is our decorator which accept function as argument	
def smartSub(fptr):  #here we are passing function name  as argument but function has two arguments 7,9 values with call
	print("inside smartSub");
	#define inner fun which swap nums depends on its value
	def inner(a,b):
		if a < b:
			a, b = b, a; # swap values to get positive num
		#inner fun calls our sub fun & return
		print("inside inner")
		return fptr(a,b);	# calling to sub function
	
	#return inner fun
	print("before return");
	return inner;  #calling to inner function

###################################################################

sub = smartSub(sub); #smartSub is decorator where we are passing name/address of SUB funcation smartSub decorator


#Now we can call sub function which is our decorated function.

print(sub(7,9)) # this call goes to smartSub with this values,this values goes with function name
