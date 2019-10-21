'''
accept person age with command line argument and display its Premium Amount

if age <= 0  # invalid input

if age > 0 and age < 20:
#2000
elif age >= 20 and age<35:
#3500
elif age >=35 and age < 50:
#5000
elif age >=50 and age<75:
#7500
else:
#10000

'''


def Dis_Premium(Age):
	ival=0;
	if(Age <= 0):
		return -1;
	
	if Age > 0 and Age < 20:
		return 2000;
	elif Age >= 20 and Age < 35:
		return 3500;
	elif Age >=35 and Age < 50:
		return 5000;
	elif Age >=50 and Age < 75:
		return 7500;
	else:
		return 10000;


import sys;
def main():
	
	myAge = int(sys.argv[1]);
	result = Dis_Premium(myAge);
	if result == -1:
		print("Invalid input");
	else:
		print("your premium amount is :",result);
		

if __name__ == '__main__':
	main();
