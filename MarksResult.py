'''
accept total marks from user and obtained markes from user and display its result

less 35 Failed
greater than 35 and less 50 ----> pass
greater than 50 and less 60 ----> pass in Second Shrenee
greater than 60 and less 75 ----> First class
greater than 75 	    ----> First class with distinction

'''

import sys;

def Grade_Gen(Total, Obt):
	iResult = (Obt/Total)*100;
	return iResult;	



def main():
	Tot = int(sys.argv[1]);
	obt = int(sys.argv[2]);
	
	if(Tot > obt):
		result = Grade_Gen(Tot,obt);
		
		if result < 35:
			print("Failed");
		elif result >=35 and result < 50:
			print("pass ");
		elif result >=50 and result < 60:
			print("pass in Second Shrenee");
		elif result >= 60 and result < 75:
			print("First class");
		else:
			print("First class With Distincation"); 
	else:
		print("invalid input");
	
		
	

if __name__ == '__main__':
	main();
