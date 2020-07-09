# here we add sum function as helper fun

def accept_data():
	
	size = int(input("Enter list size: "));
	arr = list(); #created obj of list class
	print("Enter elements for list");
	
	for i in range(0,size):
		no = int(input("Enter element: "));
		arr.append(no);
	
	return arr;


def chkEven(no):
	if no % 2 == 0:
		return True;
	else:
		return False;

def modify(no):
	return no + 2;

def add(no1, no2):
	return no1 + no2;

