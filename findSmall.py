'''
accept two list from user and display smallest element from both list

l1 = [4,5,3,1]  1
l2 = [42,22,555,34,]  22

'''

def smallFind(arr1, arr2):
	
	ismall1 = arr1[0];
	ismall2 = arr2[0];

	ilen = 0;

	if ilen < len(arr1):
		ilen = len(arr1);

	if ilen < len(arr2):
		ilen = len(arr2);
	
	for i in range(ilen):

		if i < len(arr1):

			if ismall1 > arr1[i]:
				ismall1 = arr1[i];

		if i < len(arr2):
			if ismall2 > arr2[i]:
				ismall2 = arr2[i];


	print(arr1);
	print("from first list Small found: ",ismall1);

	print(arr2);
	print("from second Small found: ",ismall2);


def main():

	size1  = int(input("enter size of first list: "));
	size2  = int(input("enter size of second list: "));

	arr1 = []
	arr2 = []

	print("Enter values for first list: ");
	for i in range(size1):
		arr1.append(int(input("Enter num: ")));

	print("Enter values for second list: ");
	for i in range(size2):
		arr2.append(int(input("Enter num: ")));
	
	smallFind(arr1, arr2);


if __name__ == "__main__":
	main();