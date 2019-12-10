'''
3. Design automation script which accept directory name from user and create log file in that directory which 
contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.

'''

import sys,psutil,os,time

def processInfo(DirName):

	if not os.path.isdir(DirName):
		os.makedirs(DirName);

	filename = "Logfile.txt";
	filename = os.path.join(DirName, filename);
	icnt = 0;
	fobj = open(filename,'w');
	seperator = ("-"*80+"\n")
	fobj.write(seperator);
	fobj.write("Running Process logger: %s"%time.ctime());
	fobj.write("\n"+seperator);

	for proc in psutil.process_iter(attrs =["pid","name","username"]):
	
		txt = str(proc.info);
		fobj.write(txt);
		fobj.write("\n");
		icnt = icnt + 1;

	fobj.write("Total Processing Running on Machine are: %s"%icnt);
	fobj.close();


def main():

	print("Application Name:",sys.argv[0]);

	if len(sys.argv) != 2:
		print("Invalid input");
	
	processInfo(sys.argv[1]);

if __name__ == "__main__":
	main();
	print("Successfully Logfile craeted");