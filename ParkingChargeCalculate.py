'''
2. Parking charges for four whaler is 30 rupees for first three
hours and after every hour it is 5 rupees. Accept number of hours
and calculate total amount.
Input  : 2
Output : 30
Input  : 7
Output : 50
'''


def ParkingChargeCal(iNo):
	
	if iNo <= 3:
		return 30;
	else:
		return 5*(iNo-3)+30;


def main():
	hr = int(input("Enter hours: "));
	res = ParkingChargeCal(hr);
	print("Total amount to be paid : ",res);


if __name__ == "__main__":
	main();
