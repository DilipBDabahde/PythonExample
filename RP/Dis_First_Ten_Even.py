'''
9. Write a program which display first 10 even numbers on screen.
output: 2 4 6 8 10 12 14 16 18 20
'''

def dis_first_ten_even():
	i = 1;
	j = 0;
	
	while(i):
		if i % 2 == 0:
			print(i);
			j = j + 1;
		
		if j == 10:
			break;
		
		i = i + 1;
		
			

def main():
	
	dis_first_ten_even();


if __name__ == "__main__":
	main();
	
	
