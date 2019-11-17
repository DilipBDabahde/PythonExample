'''
2.Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”

'''


from threading import *



def EvenFactor(num):
	isum = 0;
	for i in range(1,num):
		if ((num % i == 0) and (i % 2 == 0)):
			isum += i;
	
	print("Even Factors sum is:",isum);
	



def OddFactor(num):
	isum = 0;
	for i in range(1,num):
		if num % i == 0 and i % 2 != 0:
			isum += i;
	
	print("Odd Factors sum is:",isum);
	



def main():
	
	intval = int(input("Enter int val: "));
	
	evenfactor = Thread(target=EvenFactor, args=(intval,));
	oddfactor  = Thread(target=OddFactor, args=(intval,));
	
	#EvenFactor(intval);
	#OddFactor(intval);
	
	#below threads are used to call methods
	evenfactor.start();
	oddfactor.start();
	
	# after completing task of thread it should rejoin to its parent method by using join(); method
	
	evenfactor.join();
	oddfactor.join();	
	
	
if __name__ == "__main__":
	main();
	print("Exit from main");
