'''
script to display process all running process

'''


import psutil


def DisplayProcess():
	
	listprocess =[];

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ["pid","name","username"]);
			listprocess.append(pinfo);
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
			
	return listprocess;




def main():
	print("Displaying Running process");
	
	listprocess = DisplayProcess();
	
	for elem in listprocess:
		print(elem);	

if __name__ == '__main__':
	main();
