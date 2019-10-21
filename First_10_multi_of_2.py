'''
write a program which will display first 10 multi of 2

output: 2 4 6 8 10 12 14 16 18 20

'''

def MultiBy2():
	i=10;
	j=1;	
	while i > 0:
		if j % 2 ==0:
			print(j,"",end="");
			i-=1;
		j+=1;
	print("");
	

def main():
	MultiBy2();
	

if __name__ == '__main__':
	main();
