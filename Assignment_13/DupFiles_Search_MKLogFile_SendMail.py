'''
rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

Design automation script which performs following task.

Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.

Create one Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted. 

Name of that log file should contains the date and time at which that file gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific
time interval.

Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things :
Starting time of scanning
Total number of files scanned
Total number of duplicate files found
Consider below command line options for the gives script



Note :
For every separate task write separate function.
Write all user defined functions in one user defined module.
Use proper validation techniques.
Provide Help and usage option for script.
Create one Readme file which contains description of our script, details of command line options.
'''

from Helper_Functions import *

Scanner = 0

def main():
	
	global Scanner;
	
	print("Application name: ",argv[0]);
	print("Enter -h or -H for help");
	print("Enter -u or -U for usage");
	
	if argv[1] == '-h' or argv[1] == '-H':
		help();
		exit();
	
	if argv[1] == '-u' or argv[1] == '-U':
		usage();
		exit();
	
	try:
		
		schedule.every(int(str(argv[3]))).minutes.do(lambda : DeleteDups(argv[1], argv[2]))
		
		i = 1
		while True:
			print(i)
			i += 1;
			schedule.run_pending();
			time.sleep(1);
		
		
	
	except Exception as e:
		print("Exception occured at "+e);
		

if __name__ == "__main__":
	main();
