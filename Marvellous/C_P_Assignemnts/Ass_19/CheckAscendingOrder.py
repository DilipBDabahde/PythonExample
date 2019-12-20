'''
accept list from user and check that list is in ascending order or not

int arr= [1,2,3,4]  True
int arr= [2,4,1,5]  False

'''

def CheckOrder(listx):

	ilen = len(listx);
	if ilen == 1:
		return True;
	i = 0;
	while i < ilen-1:
		if listx[i] > listx[i+1]:
			break;
		i = i + 1;	

	#i = i + 1;
	if i == ilen-1:
		return True;
	else:
		return False;


def main():
	
	size = int(input("Enter list size: "));

	arr = [];

	for i in range(size):
		arr.append(int(input("Enter num: ")));

	

	res = CheckOrder(arr);
	if res == True:
		print("Given list is in ascending order");
	else:
		print("Given list is not in asceending order");


if __name__ == "__main__":
	main();