# imp module for threadignn is "threading"
# we created 3 threads and they work parallel

import threading


print("Demo of multithreading");


def fun(num):
	for i in range(num):
		print('A');


def gun(num):
	for i in range(num):
		print('B');
		
def sun(num):
	for i in range(num):
		print('C');


def main():
	number = 5;
		
	t1= threading.Thread(target=fun, args=(number,));
	t2= threading.Thread(target=gun, args=(number,));
	t3= threading.Thread(target=sun, args=(number,));
	#will execute both in parrallel
	t1.start();
	t2.start();
	t3.start();
	
	#join threads back to the parent process which is this
	t1.join();
	t2.join();
	t3.join();
	
	
if __name__ == '__main__':
	main();

