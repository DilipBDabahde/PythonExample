'''
accept file from user and return number of words count from that file

input : Demo.txt
		
		Demo.txt 	contains 		"here is a team which is preparing for game"

output: 9

'''

import sys,os

def CountWordOfFile(flname):
	
	icnt = 1;
	
	fd = open(flname,'r');
	print(fd.read());
	fd.seek(0);
	txt=list(fd.read())

	for i in txt:
		if i == ' ':
			icnt = icnt + 1;
	
	print("Total words are:", icnt);
	


def main():

	print("Appliation Name: ",sys.argv[0]);
	res = CountWordOfFile(sys.argv[1]);


if __name__ == "__main__":
	main();


