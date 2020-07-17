'''
create log file of all running processes of our memory and this logfile should create by perticular time by sheduling time. given timewise our script help to get logfile by scheduler

'''
import schedule
import psutil
from sys import *
import time


def Process_SnapShots():
	i = 0
	fd = open("Schd_LogFile.text", 'w');
	fd.write("Schedule wise logfile is created: %s\n"% time.ctime());
	
	for proc in psutil.process_iter():
		fd.write(str(proc.as_dict(attrs = ['pid','name','username']))+"\n");	
		i += 1;
	
	fd.write("Running processes count is: "+str(i));
	fd.close();
	
	print("Logfile of running processes schedule wise created");


def main():
	
	print("Applicationn name: "+argv[0]);
	print("for help Enter: `-h` or `-H`");
	print("for usage Enter : '-u' or '-U'");
	
	if argv[1] == '-h' or argv[1] == '-H':
		print("This script required CLI input as: python3 file.py  12:00 ");
		exit();
			
	if argv[1] == '-u' or argv[1] == '-U':
		print("Usage: This script is used to get logfile of all running processes by scheduling algorith");
		exit();
		
	if len(argv) != 2:
		print("Invalid input");
		exit();
	
	try:		
		schedule.every(1).minutes.do(Process_SnapShots);		
	
		while True:
			schedule.run_pending();
			time.sleep(1); #take rest for 1 sec and run	
		
		
	except Exception as e:
		print("Exception error "+e);

if __name__ == "__main__":
	main();
