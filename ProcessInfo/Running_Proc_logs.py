'''
creating log files of all running processes

'''
		
import psutil
import time


def Display_RunningProc():
	

	fd = open("ABC.text",'w');
	fd.write("All runnig processes of our machines\n");
	for proc in psutil.process_iter():
		fd.write(str(proc.as_dict(attrs = ['pid','name','username',]))+'\n');	
	fd.close();
	
	print("LogFile is created Successfully");
		

def main():
	st = time.time();
	Display_RunningProc();
	et = time.time();
	
	print("Time consumed for this process snapshot is: "+str(et - st));
	
if __name__ == '__main__':
	main();
	
