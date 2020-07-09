#decorator usage with addition demo


def add(a, b):
	return a + b;	# returning to inner fucntion return statement


def smartAdd(fptr):	
	def inner(a, b):
		if a < 0 or b < 0:	# to get positive out in this if we convert negative to positive
			if a < 0:
				a = -a;
			
			if b < 0:
				b = -b;		
		return fptr(a, b);	#calling add function , after coming back to this return it sends output to smartAdd rtn
				
	return inner; # calling inner fucntion, here inner fun return outout that pass to caller


add = smartAdd(add);
print("Addition is: ",add(-4,3));
print("Addition is: ",add(19,10)); # caller get return value from smartAdd zigzag way
