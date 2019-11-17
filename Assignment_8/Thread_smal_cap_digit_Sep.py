'''
4.Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.

input:: Enter string : dilipABC123
output:
Total small letters:  ['d', 'i', 'l', 'i', 'p']
Total Capital letters:  ['A', 'B', 'C']
Total Digits letters:  ['1', '2', '3']

'''


import threading


def small(line):
	sm=[];
	for i in range(len(line)):
		if line[i]>= 'a' and line[i]<= 'z':
			sm.append(line[i]);
	
	print("Total small letters: ",sm);


def capital(line):
	sm=[];
	for i in range(len(line)):
		if line[i]>= 'A' and line[i]<= 'Z':
			sm.append(line[i]);
	
	print("Total Capital letters: ",sm);


def digits(line):
	sm=[];
	for i in range(len(line)):
		if line[i]>= '0' and line[i]<= '9':
			sm.append(line[i]);
	
	print("Total Digits letters: ",sm);




def main():
	
	vakkya = input("Enter string : ");
	
	ssmall = threading.Thread(target=small, args=(vakkya,));
	ccapital = threading.Thread(target=capital, args=(vakkya,));
	ddigits = threading.Thread(target=digits, args=(vakkya,));	
	
	ssmall.start();
	ccapital.start();
	ddigits.start();
	
	print("ssmall thread id=",id(ssmall)," name=",threading.currentThread().getName());
	print("ccapital thread id=",id(ccapital)," name=",threading.currentThread().getName());
	print("ddigits thread id=",id(ddigits)," name=",threading.currentThread().getName());
	
	

if __name__ =="__main__":
	main();
	
	
