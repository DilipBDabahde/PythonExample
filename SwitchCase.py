'''
accept city code from user using Command line argu and display its city such as 20 , 02, 13 ,15,12
input:MH20
output: Aurangabad

input:MH12
output: Pune

input: MH14
output: Chinchwad

input:MH16
output:Srirampur

input:MH01
output: Mumbai

input: MH15
output:Nashik
'''

def DisplayCity(ino):
	
	switcher={20:"Aurangabad",12:"Pune",16:"Shrirampur",14:"Chinchwad",1:"Mumbai",15:"Nashik",10:"Satara",9:"Kolhapur"}
	
	return switcher.get(ino,"No Entry Available");	

import sys;
def main():
	
	Code = int(sys.argv[1]);
	x = DisplayCity(Code);
	print(x);

if __name__ == "__main__":
	main();




















