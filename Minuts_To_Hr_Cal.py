'''
Write a program which accept number of minutes and calculate
number of hours.
Input  : 320
Output : 5 hours 20 minutes
Input  : 150
Output : 2 hours 30 minutes
'''

def Minuts_to_HR(iNo):
	hr = 60;
	i = 1;
	while i * hr <= iNo:
		i += 1;
	
	return i-1,iNo % 60;

def main():
	
	mnts = int(input("Enter minuts: "));
	res1,res2 = Minuts_to_HR(mnts);
	
	print("Total HR and Minuts:[",res1,":",res2,"]");

if __name__ == "__main__":
	main();
