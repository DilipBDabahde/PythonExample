'''
write python script which will send mail automatically

'''

import sys
import urllib.request as urllib2


def is_connected():
	
	try:
		urllib2.urlopen("http://216.58.192.142",timeout=1);
		return True;
	except urllib2.URLError as err:
		return False;
		

def main():

	print("Application Name: ",sys.argv[0]);
	
	try:
		
		connected = is_conntected();
	
	if connected:
		print("done");
	else:
		print("There is no internet conntection...");



if __name__ == "__main__":
	main();
