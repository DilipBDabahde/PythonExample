"""
9.Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
"""


def First_10_Even():
	x=y=1;
	
	while x <= 10:
		if y % 2 == 0:
			print(y);
			y += 1;
			x += 1;
		else:
			y +=1;
		    

def main():
	First_10_Even();
	

if __name__ == "__main__":
	main();
