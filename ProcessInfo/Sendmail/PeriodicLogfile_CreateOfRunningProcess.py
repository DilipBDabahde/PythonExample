'''
write script which create periodic log file of RAM 

'''
import sys
import psutil
import schedule	
import time
import urllib2
import os



def ProcessLog(log_dir = "Logger"):
	print("Inside Processlog1")
		
	if not os.path.exists(log_dir):
		os.mkdir(log_dir);
	
	seperator= ("-"*80);
	log_path = os.path.join(log_dir,"Logfile %s.txt"%time.ctime());
	fobj = open(log_path,'w');
	fobj.write(seperator+"\n")	
	fobj.write("Process Running on RAM Logger Report "+time.ctime()+"\n")	
	fobj.write(seperator+"\n")	

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username']);
			fobj.write(str(pinfo));
			fobj.write("\n");
			
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass		
	
	fobj.close();	
	print("Inside Processlog7")
	print("Logfile is successfully generated at location %s"%log_path);

	

def main():
	
	print("Application Name: ",sys.argv[0]);
	
	if len(sys.argv) != 2:
		print("Invalid input");
		print("input like  .py  timein---> minutes like 1 or 2 or ......");
		exit();			
	
	try:
		schedule.every(10).minutes.do(ProcessLog);
	
		while(1):
			schedule.run_pending();
			time.sleep(1);
			
	except Exception as E:
		print("Exception occured", E);



if __name__ == "__main__":
	main();
