'''
accept list from user and return largest num and smallest num from them
input: 45 56  554 664 25 69 74 524 544 524 423
output: largest num- 664
		smallest num- 25
'''



def Large_Small_Num(ListA):

	imax=imin= ListA[0];
	i = 0;
	while i < len(ListA):
		
		if ListA[i] < imin:
			imin = ListA[i];
		elif ListA[i] > imax:
			imax = ListA[i];
		
		i = i + 1;
	
	
	print("imaxNumber is: ",imax);
	print("iminNumber is: ",imin);


def main():

	listx = [];
	size = int(input("Enter size oflist: "));
	for i in range(size):
		listx.append(int(input("Enter Num: ")));
	
	Large_Small_Num(listx);
	
if __name__ == "__main__":
	main();
