'''
accept two list from user and form new list

arr1 = [1,2,3]
arr2 = [2,4]

newFormed = [1,2,3,2,4];

'''

def formNewList(arr1, arr2):
	arr3 = [];
	j = i = 0;
	ilen = len(arr1)+len(arr2);

	while  i< ilen:
		
		if i < len(arr1):
			arr3.append(arr1[i]);
		else:
			arr3.append(arr2[j]);
			j = j + 1;

		i = i + 1;

	return arr3;

def main():
	
	size1 = int(input("Enter size of first list: "));
	size2 = int(input("Enter size of second list: "));

	arr1 = [];
	arr2 = [];

	print("Enter values for first list");
	for i in range(size1):
		arr1.append(int(input("Enter num: ")));

	print("Enter values for second list");
	for x in range(size2):
		arr2.append(int(input("Enter num: ")));

	arr2 =formNewList(arr1, arr2);

	print("New form list is: ",arr2);


if __name__ == "__main__":
	main();