
from multiprocessing import *;

print("Demonstration of Multiprocessing");

def fun(num):
	print("parent process of fun: ",os.getppid());
	print("process id of fun:",os.getpid());
	for i in range(num):
		print(i);
	

def gun(num):
	print('parent process of gun: ',os.getppid());
	print('process id of gun:',os.getpid());
	for i in range(number):
		print(i);

print("total cores available: ",multiprocessing.cpu_count())
print("process id of main:",os.getpid());
number=4;
result=None;

p1= Process(target=fun, args=(number,));
p2= Process(target=gun,args=(number,));

p1.start();
p2.start();

