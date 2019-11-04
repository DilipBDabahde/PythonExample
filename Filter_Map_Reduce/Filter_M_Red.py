from My_F_M_R import *


def AcceptData():
	
	
	size = input("Enter list size: ");
	print("Enter values for list");
	arr = list();
	
	for i in range(int(size)):
		no = int(input("Num ["+str(int(i+1))+"]:"));
		arr.append(no);
	
	print("list is---> ",arr);
	return arr;


def main():

	arr = AcceptData();
	
	FilterUpdatedData = list(filter(MyFilter,arr));
	print("UpdatedData is ",FilterUpdatedData);
	
	MapUpdatedData = list(map(MyMap,FilterUpdatedData));
	print("Updated map is ",MapUpdatedData);
	
	ReduceAns = reduce(MyReduce,MapUpdatedData);
	print("Final result is :",ReduceAns);
	

if __name__ == '__main__':
	main();
	
