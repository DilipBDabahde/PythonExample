'''
4. Design automation script which accept two directory names and one file extension. Copy all files with the specified
extension from first directory into second directory. Second directory should be created at run time.
Usage : DirectoryCopyExt.py Demo Temp  .exe
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp.

in this script we have to take first directory name which is existing in, and one non-existing dire name and take one .extension name and copy all files from existing dir to non-existing dir with given .extension


Avail DirName
		a.c 
		b.c
		k.js

Non Avail Dir			Extension    .cpp
		a.cpp
		b.cpp
		k.cpp
				conversion should be taken place after running our script
'''


import sys
import shutil
import os



def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
    	
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:   
            	if not os.path.isabs(s):
					s = os.path.abspath(s);	
					shutil.copy2(s, d);
					
					
					
					
def Extension_Changer(path, ext):
	flag = os.path.isabs(path);			
	if flag == False:
		path = os.path.abspath(path);
	
	os.chdir(path);
	
	for f in os.listdir(path):
		file_name, file_ext = os.path.splitext(f);
		f = os.path.join(path,f);
		os.rename(f, str(file_name)+ext);
					
					

def main():

	print("Application Name:",sys.argv[0]);
	
	if len(sys.argv) != 4:
		print("Invalid input");
	try:	
		copytree(sys.argv[1],sys.argv[2]);
		Extension_Changer(sys.argv[2], sys.argv[3]);		
	except Exception as e:
		print("Error Found ",e);

if __name__ == "__main__":
	main();
