'''
write script which accept directory name from user if that dir is exists or not check, if it's not existing then makedirs then create Logfile.txt of RAM Snapshot into file as per scheduler schedule

'''

import time,schedule,sys,os,psutil



def Writer(path):
	
	global icnt;
	if not os.path.exists(path):
		os.mkdir(path);  # os.makedirs(path);
	
	logfile = "Logfile%s.txt"%time.ctime();
	 
	if not os.path.isabs(logfile):
		logfile = os.path.join(path,logfile); 
	
	fobj = open(logfile,'w');
	fobj.write("-"*80);
	fobj.write("\n Running Process Logger %s\n"%time.ctime());
	fobj.write("-"*80);
	fobj.write("\n");
	
	
	for pobj in psutil.process_iter():
		txt = str(pobj);
		fobj.write(txt);
		fobj.write("\n");		
	fobj.close();


def main():

	print("Application Name:",sys.argv[0]);
	
	if len(sys.argv) != 2:
		print("Invalid input");
		print("Input like  .py DirName");
		exit();
	print("Taking Snapshots ..............");
	try:
		schedule.every(1).minutes.do(Writer,path=sys.argv[1]);
		schedule.every(5).minutes.do(Writer,path=sys.argv[1]);
		schedule.every().hour.do(Writer,path=sys.argv[1]);
	
		while True:
			schedule.run_pending();
			time.sleep(1);
	
	except Exception as E:
		print("Exception occured",E);
		

if __name__ == "__main__":
	main();
