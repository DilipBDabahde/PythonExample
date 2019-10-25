#check given input is contact number or not

def isPhoneNum(text):
	if len(text) != 12:
		return False;
	for i in range(0,3):
		if not text[i].isdecimal():
			return False;
	
	if text[3] != '-':
		return False;
	
	for i in range(4,7):
		if not text[i].isdecimal():
			return False;
			
	if text[7] != '-':
		return False;
	
	for i in range(8,12):
		if not text[i].isdecimal():
			return False;
	return True;


print('415-555-4242 is a phone number')
print(isPhoneNum('415-555-4242'))

print('Moshi Moshi is a phone number:')
print(isPhoneNum('Moshi moshi'))
