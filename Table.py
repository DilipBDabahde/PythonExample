'''
accept num from user and print its table till 10

input: 12
output: 12 24 36 48 60 72 84 96 108 120

input:6
output: 6 12 18 24 30 36 42 48 54 60

for this program take input as command line argument
'''


import sys;

def table(iNo):
	
	for i in range(1,11):
		print(iNo*i);
	print("");

def main():
	ival = int(sys.argv[1]);
	table(ival);


if __name__ == "__main__":
 	main();


