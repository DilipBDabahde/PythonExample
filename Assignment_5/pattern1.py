'''
2. Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
'''

i = 1;

def pattern(iNo):
	global  i;
	
	if i <= iNo:
		print(i,end= " ");
		i += 1;
		pattern(iNo);
		

def main():
	
	val = int(input("Enter a val:"));
	pattern(val);
	print();

if __name__ == '__main__':
	main();
	
