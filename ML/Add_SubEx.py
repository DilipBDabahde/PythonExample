

class Readfile:

	def __init__(self, first, second):
		
		self.v1 = first;
		self.v2 = second;

	def add(self):
		return self.v2+self.v1;

	def sub(self):

		if self.v1 > self.v2:
			return self.v1 - self.v2;
		else:
			return self.v2 - self.v1;


def main():

	val1 = int(input("Enter first number: "))
	val2 = int(input("Enter second number: "))

	line = "-"*44;
	obj = Readfile(val1, val2);
	res = obj.add();
	print("Sum of given number is: ",res);
	print(line);

	print("Enter two values for subtraction: ")
	val1 = int(input("Enter first number: "))
	val2 = int(input("Enter second number: "))

	obj1 = Readfile(val1, val2);
	res = obj1.sub();
	print("Sub of given two values is: ",res);



if __name__ == "__main__":
		main();