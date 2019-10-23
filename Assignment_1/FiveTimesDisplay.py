"""
4.Write a program which display 5 times Marvellous on screen.
Output :
Marvellous
Marvellous
Marvellous
Marvellous
Marvellous

"""



def DisplayN(iNo):
	
	for i in range(0,iNo):
		print("Marvellous");
	

def main():
	
	ival = int(input("Enter a Number: "));
	DisplayN(ival);

if __name__ == "__main__":
	main();
