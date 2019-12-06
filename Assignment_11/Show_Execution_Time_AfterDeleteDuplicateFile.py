'''
4. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of
duplicate files from that directory into log file named as Log.txt.

Log.txt file should be created into current directory. Display execution time required for the script.
Usage : DirectoryDusplicateRemoval.py "Demo"
Demo is name of directory.				
			
'''


import os,time,hashlib,sys

def CheckSumCreator(path):		# this function help to return file checksum
	fobj = open(path,'rb');
	txt = fobj.read()
	return hashlib.md5(txt).hexdigest();
		


def DislayFiles(path):	# accept dir name display files
	print("---we are in given directory---",path);
	
	orgfile = "original.txt";
	dupfile = "Duplicate.txt";
	fobj = open(dupfile,'w');
	fobj.close();
	
	fobj = open(orgfile,'w');
	fobj.close();
	
	chk = None;
	icnt1 = 0;
	icnt2 = 0;
	dict1 = [];	# empty creation
	
	if not os.path.isdir(path):
		path = os.path.abspath(path);
		print(path);
	
	for folder, subfolders, filelist in os.walk(path):
		for filename in filelist:
			if not os.path.isabs(filename):
				filename = os.path.join(folder,filename);
		
				chk = CheckSumCreator(filename);
				if not chk in dict1:
					dict1.append(chk);
					fb = open(orgfile,'a');
					fb.write(filename);
					fb.write("\n")
					fb.close();
					icnt1 = icnt1 + 1;
				
				else:
					print(filename, chk);
					fb = open(dupfile,'a');
					fb.write(filename);
					fb.write("\n")
					fb.close();
					os.remove(filename);
					icnt2 = icnt2 + 1;
				

	fb = open(dupfile,'a');
	fb.write("Total duplicate files are: %s " %str(icnt2));
	fb.close;
	
	fb = open(orgfile,'a');
	fb.write("Total origial files are: %s "%str(icnt1));
	fb.close();

	
def main():
	
	print("Application name: ",sys.argv[0]);
	
	if len(sys.argv) != 2:
		print("Invalid input: ");
		exit();
	
	try:
		st = time.time();
		DislayFiles(sys.argv[1]);
		et = time.time();
		
		print("Execution time taken",et - st);
		
	except Exception as e:
		print("Exception occured",e);
	
	


if __name__ == "__main__":
	main();

