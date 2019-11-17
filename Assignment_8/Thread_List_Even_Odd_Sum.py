'''
3.Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
'''

import threading



def EvenList(listxx):
	isum = 0;
	for i in range(len(listxx)):
		if listxx[i]%2==0:
			isum += listxx[i];
	
	print("Sum of all Even nums is: ",isum);


def OddList(listxx):
	isum = 0;
	for i in range(len(listxx)):
		if listxx[i]%2 !=0:
			isum += listxx[i];
	
	print("Sum of all Odd nums is: ",isum);


def main():

	size = int(input("Enter size of list: "));
	listx=[];
	for i in range(size):
		listx.append(int(input("Enter num: ")));
	
	print("Given list is: ",listx);
	
	evenlist = threading.Thread(target = EvenList, args=(listx,));
	oddlist = threading.Thread(target = OddList, args=(listx,));
	
	#EvenList(listx);
	#OddList(listx);
	
	# using threads to call above defined methods indirectly with start()
	
	evenlist.start();
	oddlist.start();


if __name__ == "__main__":
	main();
