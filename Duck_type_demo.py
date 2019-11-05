print("demo of Duck typing");

class Sparrow:		#class Definition
	def fly(self):	#function def with a parameter
		print("Sparrow flying");


class Airplane:
	def fly(self):
		print("Airplane flying");


class Whale:
	def swim(self):
		print("Whale smimming");



def fun(entity):	# getting id of function which are declared in classes above
	entity.fly();	# calling the function as per their id
	


def main():
	
	sparrow = Sparrow();
	airplane=Airplane();
	whale=Whale();

	fun(sparrow);	#print 'Sparrow flying'
	
	fun(airplane);	#print 'Airplane flying'
	
	#fun(whale);		# fly is not define in Whale class   <<  --- remove comment for this line it will give error
	

if __name__ == "__main__":
	main();
	



