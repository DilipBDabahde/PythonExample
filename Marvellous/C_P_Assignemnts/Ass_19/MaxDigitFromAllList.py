'''
1.Accept N numbers from user and display such a digit which occurs  maximum number of time in list.

we have 9 elemts array so find from all elements max digit count

input: Arraysize 9
		{745,655,362,243,121,102,4324,123,,532}
		1 = 4
		2 = 7
		3 = 5
		4 = 3
		5 = 4
		6 = 2
		7 = 1
		8 = 1
		9 = 0
		0 = 1

ouput: 7
'''



def MaxDigitcount(arr):

	brr = [0]*10; # creating new list for finding max digit
	
	for i in arr:
		itemp = i;
		while itemp != 0:
			brr[itemp%10] += 1;
			itemp = int(itemp/10);

	print(arr)
	print(brr);
	icnt = 0;
	imax = 0
	
	for i in range(len(brr)):
		if brr[i] > imax:
			imax = brr[i];
			icnt = i;

	return icnt;


def main():

	size = int(input("Enter size of List: "));
	arr = []; #emppty list
	for i in range(size):
		arr.append(int(input("Enter num:")));

	result = MaxDigitcount(arr);
	print("Maxtime  found digit from whole list is: ",result);


if __name__ == "__main__":
	main();