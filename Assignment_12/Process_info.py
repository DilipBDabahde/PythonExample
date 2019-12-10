'''
1.Design automation script which display information of running processes as its name, PID,
Username.
'''

import sys
import psutil

def ProcessInfo():
	list = [];

	for proc in psutil.process_iter(attrs =["pid","name","username"]):
		print(proc.info);
'''
procs = {p.pid:p.info for p in psutil.process_iter(attrs = ['name','username'])}

for i in procs:
	print(procs[i]);
'''
def main():

	print("Application Name:",sys.argv[0]);
	ProcessInfo();



if __name__ == "__main__":
	main();