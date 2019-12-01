'''
4.Write a program which accept two file names from user and compare contents of both the files. If both the files 
contains same contents then display success otherwise display failure.Accept names of both the files from command line.

Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt

'''

import sys,os



def CmpTwoFile(f1, f2):
	icnt = 0;
	ls1 = list();
	ls2 = list();
	
	if os.path.exists(f1) and os.path.exists(f2):
		exists = True;
	else:
		exists = False;
	
	if exists == True:
		with open(f1,'r')as f1:
			with open(f2,'r')as f2:
		
				txt1=f1.read();
				txt2=f2.read();		
				
			for i in range(len(txt1)):
				ls1.append(txt1[i]);	
			
			for i in range(len(txt2)):
				ls2.append(txt2[i]);
			
			
			if len(ls1) == len(ls2):
				
				for i in range(len(ls1)):
					if ls2[i] == ls1[i]:
						icnt = icnt + 1;
					else:
						break;
					
				if icnt == len(ls1):
					print("Both given files are having same contents");
				else:
					print("Both given files are not having same contents");
	
			else:
				print("Both given files are not having same contents");
	else:
		print("Gvien files does not exits")

def main():
	
	print("Application Name: ",sys.argv[0]);
	print("First file name: ",sys.argv[1]);			# create az.txt with some text
	print("Second file name: ",sys.argv[2]);		# create za.txt with some text
	
	CmpTwoFile(sys.argv[1],sys.argv[2]);
	


if __name__ == "__main__":
	main();
