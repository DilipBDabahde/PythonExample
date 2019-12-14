'''
Automation script which accept file name. Extract all URLs from that file and connect to that URLs
for this file use we have to provide url 
'''

import sys
import re
import webbrowser
import urllib2


def is_connected():
	
	try:	
		urllib2.urlopen("http://216.58.192.142",timeout=1);
		return True;
	except Exception as E:
		return False;


def find(string):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]|[0-9a-fA-F]))+',string);
	return url;



def WebLauncher(path):
	with open(path) as fp:
		for line in fp:
			print(line);
			url = find(line);
			print(url);
			for str in url:
				webbrowser.open(str,new=2);


def main():

	print("Application Name: ",sys.argv[0]);
	
	
	if len(sys.argv) != 2:
		print("Error: invalid inputs")
		exit();
		
	if sys.argv[1] == 'u' or sys.argv[1] == 'H':
		print("This script is used open URL which are writtern in one file")
		exit();
		
	try:		
		connected = is_connected();		
		if connected:
			filename = sys.argv[1];
			print(filename);
			WebLauncher(sys.argv[1]);
		else:
			print("No internet connection...");
	
	except Exception as E:
		print("Exception occured",E);		
		
if __name__ == "__main__":
	main();
