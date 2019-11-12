'''
Write a program which accept number of hours and calculate
number of minutes
input: 4
output: 240
'''

def MinutsCnt(iNo):
	return iNo * 60;


def main():
	val = int(input("Enter a val: "));
	res = MinutsCnt(val);
	print("Total minuts found :",res);


if __name__ == "__main__":
	main();
