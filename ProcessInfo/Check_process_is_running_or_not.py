'''
2.Design automation script which accept process name and display information of that process if
it is running.
Usage : ProcInfo.py Notepad

'''


import psutil
from sys import *



def CheckProcess_stats(procname):
	i = 0;

	for proc  in psutil.process_iter():
		pinfo = proc.as_dict(attrs = ['pid','username', 'name']);
		if procname in pinfo['name']:
			print("Given process name is ~ %s ~ running: "%(procname), pinfo);
			i = i + 1;
			break;
	
	if i == 0:
		print("Given process is not running");
			

def main():
	print("inside main");
	
	print("Application name: "+argv[0]);
	print("Enter -h or -H for help");
	
	
	try:
		
		CheckProcess_stats(argv[1]);
	
	except Exception as e:
		print("Exception occured "+e);



if __name__ == "__main__":
	main();

