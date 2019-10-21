# accept num from user and print even num till that num
#input:5 		output: 2 4 6 8 10


def EvenOnly(iNo):
	i = 1;
	while iNo > 0:
		if(i  % 2 == 0):
			print(i,"",end="");
			iNo-=1;
		i+=1;
	print("");
		
	
def main():
	ival = int(input("Enter a Val:"));
	EvenOnly(ival);
	

if __name__ == "__main__":
	main();
