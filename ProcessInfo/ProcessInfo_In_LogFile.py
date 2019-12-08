'''
write python script which accept dirname from user create Logfile into that directorpy dir+logfile should at runtime
'''


import sys,psutil,os,time


def ProcessWriter(path):
	
	listx = [];
	
	if not os.path.isdir(path):
		os.makedirs(path);
	
	filename = "Logfile%s.txt"%time.ctime();
	filename = os.path.join(path, filename);
	
	fobj = open(filename,'w');
	fobj.write("-"*80+"\n");
	fobj.write("Running process Logs %s\n"%time.ctime());
	fobj.write("-"*80+"\n");	
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs =["pid","name","username"]);
			
			fobj.write(str(pinfo)+"\n");
		except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
			pass	
	
	fobj.close();
	


def main():
	
	print("Application Name: ",sys.argv[0]);
	
	if len(sys.argv) != 2:
		print("Invlaid input:")
		print("Input like .py Dirname");
		exit();	
	
	try:
		
		ProcessWriter(sys.argv[1]);
	
	except AttributeError as E:
		print("Exception Occured",E);	
	except ValueError as E:
		print("Exception Occured",E);	
	except Exception as E:
		print("Exception Occured",E);

if __name__ == "__main__":
	main();

