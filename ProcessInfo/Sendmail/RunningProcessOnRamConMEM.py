'''
write script in python which display running process on RAM and usage of RAM
'''
import psutil,sys


def DisplayRunningProcessInfo():

	listx= [];
	
	try:		
		for proc in psutil.process_iter():
			pinfo = proc.as_dict(attrs = ["pid","name","username"]);
			pinfo['vms'] = proc.memory_info().vms/(1024*1024);	
			listx.append(pinfo);			
		return listx;
		
	except Exception as e:
		print("Exception occured",e )


def main():

	print("Application Name: ",sys.argv[0]);
	listx = [];
	try:
			listx = DisplayRunningProcessInfo();
	except Exception as E:
		print("Exception occured",e);
	
	for elem in listx:
		print(elem);

if __name__ == "__main__":
	main();
