import Arothmatic

def main():
	
	ival1 = int(input("Enter first value:"));
	ival2 = int(input("Enter second value:"));
	
	result = Arothmatic.Add(ival1, ival2);
	print("Addition is: ",result)
	
	result = Arothmatic.Sub(ival1, ival2);
	print("Subtraction is: ",result)
	
	result = Arothmatic.Mult(ival1, ival2);
	print("Multiplication is: ",result)
	
	result = Arothmatic.Div(ival1, ival2);
	print("Division is: ",result)
	

if __name__ == "__main__":
	main();
	
