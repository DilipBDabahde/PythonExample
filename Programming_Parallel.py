# in this program we use all cores

import multiprocessing
import os
from time import *

def square(n):
	print("Worker process id for{0}:{1}".format(n,os.getpid()));
	return (n*n);


def main():
	
	#input list
	arr=[11,22,33,44,55];
	
	# creating Pool class object
	p= multiprocessing.Pool();
	
	#mapping list to target funcion
	startime=time();
	result = p.map(square,arr);
	endtime=time();
	print("time used parallel: ",endtime-startime);
	print("Square of each elements:");
	print(result);
	
if __name__ =="__main__":
	main();
