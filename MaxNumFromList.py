'''
accept list from user and display max number from that list
input : mylist=[4,63,6,2,77,445,7,4,456,065,467,444];
output:465



mylist=[4,63,6,2,77,445,7,4,456,65,467,444];


max=0;
for i in range(len(mylist)):
	if mylist[i]>max:
		max=mylist[i];

print(max);

'''


def MaxNumFind(mylist):
	max = 0;
	for i in range(len(mylist)):
		if mylist[i]>max:
			max=mylist[i];
	return max;
	

def main():

	val = int(input("Enter size of list:"));
	list1=[];
	for i in range(val):
		no = int(input("Enter Num:"));
		list1.append(no);
	
	res = MaxNumFind(list1);
	print(list1);
	print("max num from list is: ",res);		

if __name__ == '__main__':
	main();
