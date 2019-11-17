'''
5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
'''

from threading import *

def Counter(fname,num,obj):
	fname(obj,num);	
	
	
def forward(obj,num):
	print("inside forward");
	obj.acquire(); # we got lock here
	i=1;
	while(i <= num):
		print(i,end=" ");
		i += 1;
	print();
	obj.release();

def backward(obj,num):
	print("inside backward");
	obj.acquire(); # we got lock here
	i=1;
	while(num >= i):
		print(num,end=" ");
		num -= 1;
	print();
	obj.release();
	

def main():
	# creating threads and object of Lock class
	
	val = int(input("Enter a val:"));	
	
	lock = Lock();		# use circular bracket to create class

	t1 = Thread(target=Counter, args=(forward,val,lock,));
	t2 = Thread(target=Counter, args=(backward,val,lock,));
	
	t1.start();
	t2.start();
	
	t1.join();
	t2.join();


if __name__ == "__main__":
	main();

