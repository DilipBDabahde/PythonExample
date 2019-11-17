# in this program we can see how to create thread and use syncronization using lock-class
import threading 

amount = 0; 	 # global var

def Counter(fun,lock):
	fun(lock);

def Credit(lock):
	value = int(input("Enter amount to creadit:"));
	lock.acquire();
	global amount;
	amount += value;
	print("Updated balance is: ",amount);
	lock.release();
	
def Debit(lock):
	value= int(input("Enter amount to withdraw:"));
	lock.acquire();
	global amount;
	if amount < value:
		print("unable to withdraw due to insuff amount");
	else:
		amount -= value;
		print("Sucessfully withdrawn ",value);
		print("your updated bal is ",amount);
		lock.release();

def main():
	
	lock = threading.Lock();
	t1=threading.Thread(target=Counter, args=(Credit,lock,));
	t2=threading.Thread(target=Counter, args=(Debit,lock,));
	
	t1.start();
	t2.start();
	
	t1.join();
	t2.join();

if __name__ =="__main__":
	main();

