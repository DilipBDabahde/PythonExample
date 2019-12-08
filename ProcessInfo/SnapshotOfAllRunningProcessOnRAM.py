'''
write a script which display all running processes on RAM Console
'''

import sys
import time
import schedule
import psutil


def Writer():
	print("-"*80);
	print("Calling...",time.ctime());
	print("-"*80);
	for pobj in psutil.process_iter():
		print(pobj);
	print('\n')

def main():

	print("Application Name: ",sys.argv[0]);
	
	try:		
		schedule.every(1).minutes.do(Writer);
		
		while(1):
			schedule.run_pending();
			time.sleep(1);
	
	except Exception as E:
		print("Exceptionn occured",E);


if __name__ == "__main__":
	main();
