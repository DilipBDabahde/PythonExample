'''
write python script which will check ur machine is connected with internet or not

'''

import sys
import urllib2


def is_connected():
	
	try:
		urllib2.urlopen("http://216.58.192.142",timeout=1);
		return True;
	except urllib2.URLError as err:
		return False;
		

def main():

	print("Application Name: ",sys.argv[0]);
	
	try:		
		connected = is_connected();
	
		if connected:
			print("your are conneced with internet...");
		else:
			print("There is no internet conntection...");

	except Exception as E:
		print("Exception Occured ",E)


if __name__ == "__main__":
	main();
