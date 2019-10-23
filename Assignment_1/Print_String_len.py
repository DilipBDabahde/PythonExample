"""
10. Write a program which accept name from user and display length of its name.
Input : Marvellous
Output : 10
"""

def DisplayLenght(Value):
	print(Value,":",len(Value));
	

def main():
	val = input("Enter name: ");
	DisplayLenght(val);
	
if __name__ == "__main__":
	main();
