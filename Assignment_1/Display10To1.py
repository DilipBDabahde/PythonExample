"""
5.Write a program which display 10 to 1 on screen.
Output : 10 9 8 7 6 5 4 3 2 1
"""



def Display():
	iNo = 10;
	
	while iNo > 0:
		print(iNo,"",end='');
		iNo -= 1;

def main():
	Display();
	print("");
	
	
if __name__ == "__main__":
	main();
