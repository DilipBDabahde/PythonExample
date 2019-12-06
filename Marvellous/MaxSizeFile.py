'''
write script in python which accept dirname from user and return maxsize file from that dir

'''

import sys,os

def MaxSZ(path):

	fileSZ = 0;
	fileNM = None

	for dir_p, dir_c, fileList in os.walk(path):
		for filename in fileList:
			flag = os.path.isdir(filename)
			if not os.path.isabs(filename):
				filename = os.path.join(dir_p, filename);
				print(filename);
				sz = os.path.getsize(filename);
				if sz > fileSZ:
					fileSZ = sz;
					fileNM = filename;	
				print("Filename = ",filename, "Filesize", fileSZ);
	return fileNM,fileSZ;			
				


def main():

	print("Application Name:",sys.argv[0]);
	
	if len(sys.argv) != 2:
		print("invalid input");
		print("Input like: .py  Dirname");
		exit()	
	
	try:
		
		print("In Given Directory MaxSizeFile is")
		filename, size = MaxSZ(sys.argv[1]);	
		print("MaxFileSize FileName = ",filename,"  Size =", size)
			
	except Exception as e:
		print("Exception occurect",e);
	



if __name__ == "__main__":
	main();
