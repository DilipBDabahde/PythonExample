'''
3.Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py Demo  Temp
Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all 
files from Demo to Temp.

input :  DirName1  DirName2
		 DirName2 shoude create at run time and copy files from DirName1
		 
		 
'''


import os
import sys
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
    	if os.path.isfile(item):
        	s = os.path.join(src, item)
        	d = os.path.join(dst, item)
        	if os.path.isdir(s):
        	    copytree(s, d, symlinks, ignore)
        	else:
        	    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
        	        shutil.copy2(s, d);   	                
        	        
        	        
def main():
	
	print("Application Name: ",sys.argv[0]);
	
	try:
		copytree(sys.argv[1],sys.argv[2]);
	except Exception as e:
		print("Error Found",e);


if __name__ == "__main__":
	main();

