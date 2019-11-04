'''
3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. Filtershould filter out all such numbers which greater than or
equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 653875200
'''

	
from functools import reduce;

def AcceptData():
	
	arr = list();
	size = int(input("Enter size of list: "));
	print("Enter values for lsit");
	
	for i in range(size):
		no = int(input("Num ["+str(int(i+1))+"]: "));
		arr.append(no);
	
	print("Our list is ready--> ",arr);
	return arr;



def main():
	
	arr = AcceptData();
	print("req num >= 70 and <= 90");
	
	MyFilter = list(filter(lambda no : (no >=70 and no <= 90),arr));
	print("Updated list is ",MyFilter);

	MyMap = list(map(lambda no: (no+10),MyFilter));
	print("Updated Map list is ",MyMap);
	
	MyReduce = reduce((lambda no1,no2:(no1+no2)),MyMap)
	print("Reduce is ",MyReduce);



if __name__ == "__main__":
	main();
