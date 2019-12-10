'''
2.Design automation script which accept process name and display information of that process if it is running.

Usage : ProcInfo.py chrome or python or cpusdp.
'''
import sys
import psutil

def find_proc_by_name(name):
		ls = [];
		icnt = 0
		for p in psutil.process_iter(attrs = ['name']):
			if p.info['name']==name:
				icnt = icnt + 1;
				ls.append(p);
		
		if icnt > 0:
			for p in ls:
				print(p);
		else:
			print("Given Process not exit....")

def main():

	print("Application name: ",sys.argv[0]);
	find_proc_by_name(sys.argv[1]);


if __name__ == '__main__':
	main()