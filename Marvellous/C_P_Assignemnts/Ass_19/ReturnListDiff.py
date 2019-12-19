'''
accept two integer list from user and return diff from both list

input: l1 = [1,5,7,3]
	   l2 = [2,6,8,4,8] 

	   l1 = 16
	   l2 = 28

	   return 28 - 16
	   = 12
'''


def ReturnDiffFromTwolist(listA, listB):
	sum1 = 0;
	sum2 = 0;

	print(listA);
	print(listB);

	for i in range(len(listA)):
		sum1 = sum1 + listA[i];

	for i in range(len(listB)):
		sum2 = sum2 + listB[i];

	if sum1 > sum2:
		return sum1 - sum2;
	else:
		return sum2 - sum1;




def main():
	
	size1 = int(input("Enter first list size: "));
	size2 = int(input("Enter second list size: "));

	ListA = [];
	ListB = [];

	print("Enter values for first list");
	for i in range(size1):
		ListA.append(int(input("Enter num: ")));

	print("Enter values for second list: ");
	for i in range(size2):
		ListB.append(int(input("Enter num: ")));

	
	result = ReturnDiffFromTwolist(ListA, ListB);
	print("Difference from both list is: ",result);


if __name__ == "__main__":
	main();