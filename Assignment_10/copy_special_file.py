'''
in this script we have to accept existing dir name which contains some files. To copy files from dirfirst to another
we have to apply filter on extension of some files which we require to copy and just before copying these files we need to created another dir as per choice

dirFirst:
	|__Files__ a.c  b.c  ab.c  j1.java j2.java j3.java   ppa1.py ppa2.py ppa3.py	 ~~ total 9 files
	
	our filter is extension of file   '.java'  
	
	those files endswith .java make copy of these files into another directory
	
anotherDir:
	|__CopyedFiles__ j1.java j2.java j3.java



in this case we are gonna copy only current dir files not child OKK...

'''

from sys import *;
import os


def copy_myfile_dirOne_to_dirSec(src, dest, ext): # targeted function
	
	if not os.path.exists(dest):	# if dest dir is not there then we create here
		os.makedirs(dest);
		
	for item in os.listdir(src):
		if item.endswith(ext):
			s = os.path.join(src, item);
			fd = open(s, 'r');
			data = fd.read();
			fd.close();
			
			fname = str(item); #just taking file name to make this name file is destination dir		
			
			d = os.path.join(dest, fname);
			fd = open(d, 'w');
			fd.write(data);
			fd.close();
	
	print("Files are copyed successfully")
			


def usage():
	print("Usage: This script is used to copyfiles from one dir to another dir with specific type of extension");


def help():
	print("To run this script input should like: python3 filename.py DemoDir TempDir  extension");
	print("DemoDir: This dir should be existing dir to perform operation on it");
	print("Tempdir: Should be created at runtime");
	print("extension: it could be any which is used to filterized files to copy");

def main():
	
	print("Application Name: ",argv[0]);
	print("Enter -h or -H for help");
	print("Enter -u or -U for to know Usage");
	
	if argv[1] == '-h' or argv[1] == '-H':
		help();
		exit();
	
	if argv[1] == '-u' or argv[1] == '-U':
		usage();
		exit();
	
	if len(argv) != 4:
		print("invalid input");
		exit();
	
	try:
		copy_myfile_dirOne_to_dirSec(argv[1], argv[2], argv[3]);
	
	except Exception as e:
		print("Exception occured" + e);


if __name__ == "__main__":
	main();
