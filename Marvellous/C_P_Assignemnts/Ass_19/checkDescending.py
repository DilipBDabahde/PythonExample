'''
accept list from user and check that listis descending order or not

list1 = [12,9,5,3,2]  True
list1 = [15,4,8,5,3]  False


'''

def checkDescending(arr):
	
	ilen = len(arr);
	i = 0;
	if len == 1:
		return True;

	while  i < ilen-1:
		if arr[i] < arr[i+1]:
			break;
		i = i + 1;

	if i == ilen-1:
		return True;
	else:
		return False;


def main():

	size = int(input("Enter list size: "));

	arr = [];

	for i in range(size):
		arr.append(int(input("Enter num: ")));

	res = checkDescending(arr);
	if res == True:
		print("Given list is descending");
	else:
		print("Gvien list is not descending");

if __name__ == "__main__":
		main();
