
def sub(no1, no2):
	return no1 - no2;


def decorator(original_function):
	
	def updator(a, b):
		if a < b:
			a, b = b, a;
		return original_function(a,b);	
	return updator;

newsub = decorator(sub);

print("Sub of 10 and 7 is: ",newsub(10,7));
print("Sub of 7 and 10 is: ",newsub(7,10));
