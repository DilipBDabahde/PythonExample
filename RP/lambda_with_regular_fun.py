#using lambda function which is also known as anonymous function


# regular function demo

def Add(no1, no2):
	ans = 0
	ans = no1 + no2;
	
	return ans;


def main():
	
	val1 = int(input("Enter first num: "));
	val2 = int(input("Enter second num: "));
	
	result = Add(val1, val2);
	print("Addition is: ", result);


#main(); # main function call

# demonstration of lambda function 
# lambda arguments : expression

print("\n\nDemonstration of Lambda\n\n")
dilip = lambda no1, no2 : no1 + no2

val1 = int(input("Enter first num: "));
val2 = int(input("Enter second num: "));

result = dilip(val1, val2);

print("Lambda making addition: ", result);


