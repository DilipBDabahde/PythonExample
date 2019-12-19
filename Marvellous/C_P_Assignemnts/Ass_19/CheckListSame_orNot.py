'''
accept two integer list from user and check both are same or not

l1 = [1,4,5,6]
l2 = [1,4,5,6]  True

l1 = [12,33];
l2 = [1,3] False

'''



def Checklist(listA, listB):

	for i in  range(len(listA)):
		if listA[i] != listB[i]:
			break;

	print(listA)
	print(listB)
	if i==len(listA)-1:
		return True;
	else:
		return False;
			

def main():

	size1 = int(input("Enter first list size: "));
	size2 = int(input("Enter second list size: "));

	list_A = [];
	list_B = [];

	print("Enter first list values");
	for i in range(size1):
		list_A.append(int(input("Enter num:")));

	print("Enter second list values");
	for i in range(size2):
		list_B.append(int(input("Enter num: ")));

	if 	size1 != size2:
		print("Given input length is invalid");
		exit();
	else:
		res = Checklist(list_A, list_B);
		if res:
			print("Given list are same");
		else:
			print("Given list are not same");


if __name__ == "__main__":
	main();