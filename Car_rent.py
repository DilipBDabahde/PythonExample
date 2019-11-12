'''
Rent of car is 15 rupees per kilometre for first 120 kilometres
and after that it is 10 rupees per kilometre. Accept total number
of kilometres and calculate rent.
Input : 80
Output: 1200
Input : 145
Output: 2050
'''

def Car_Rent_Cal(km):
	if km <= 120:
		return km * 15;
	else:
		return km * 10;


def main():
	
	km = int(input("Enter kmtrs: "));
	res = Car_Rent_Cal(km);
	print("Total bill kmwise is: ",res);
	

if __name__ == "__main__":
	main();

