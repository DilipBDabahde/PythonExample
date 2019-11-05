#creating decorator in python

print("Demonstration of Decorator");

def sub(no1,no2):		#this sub function is fix funtion   id = 100
	return no1-no2;

def Decorator(tempsub):				#id 200
	def Updator(x,y):				#id 300 this inner function help to swap nums go get possitive result
		if x < y:
			x,y=y,x;
		return tempsub(x,y);
	return Updator;



def main():

	newsub = Decorator(sub);

	res = newsub(12,4);  #two parameter passing 
	print("res is: ",res);

	res = newsub(4,12);
	print("result is: ",res);	#two parameter passing 



if __name__ == "__main__":
	main();
