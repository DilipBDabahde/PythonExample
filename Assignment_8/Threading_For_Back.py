'''
5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2
'''
import threading

def forward(iNo):
	i = 1;
	while(i<=iNo):
		print(i,end=" ");
		i = i + 1;	

def backward(iNo):
	while iNo >= 1:
		print(iNo,end=" ");
		iNo = iNo - 1;


def main():
	
	ival = int(input("Enter a Num:"));
	
	t1= threading.Thread(target=forward,args=(ival,));
	t2= threading.Thread(target=backward,args=(ival,));
	
	t1.start();
	print();
	t2.start();
	print();	
	
	t1.join();
	t2.join();
	

if __name__ == "__main__":
	main();
