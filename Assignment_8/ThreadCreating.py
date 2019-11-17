'''
1.Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
'''

from threading import *;


def Even(num):
	for i in range(num):
		if i % 2 == 0:
			print("from Even: ",i);


def Odd(num):
	for i in range(num):
		if i % 2 != 0:
			print("from Odd: ",i);


def main():
	
	even = Thread(target=Even, args=(10,));
	odd  = Thread(target=Odd, args=(10,));
	
	# after creating thread we have to call start method
	
	even.start();
	odd.start();
	# above by using created thread  we calling defined functions
	
	even.join();
	odd.join(); 
	#after completing thread task they rejoin to their parent
	#if thread is not started we are using it with join methood we will get error	
	
if __name__ == '__main__':
	main();

