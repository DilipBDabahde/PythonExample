'''
this script helps to given us perticular websites images url
Automation script which fetch URL of all images using Beautiful Soup'''

from sys import * 
import os
import bs4
import requests
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
    
    
def ImageURLScrapper(url):
	
	connection = urlopen(url);
	
	raw_html = connection.read();
	connection.close();
	page_soup = bs4.BeautifulSoup(raw_html,"html.parser");
	container = page_soup.findAll("div",{"class":"item-container"});
	
	return container;

def main():

	print("Demo of fetching url of image");
	
	print("Application name:"+argv[0]);
	
	if len(argv) == 2:
		if argv[1]=='-h' or argv[1]=='-H':
			print("This script is used to fetch url of images");
		exit();

	
	try:
		url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38";

		listout = ImageURLScrapper(url);
		
		print("URL of all images");
		for ex  in listout:
			print(ex.a.img['data-src']);
	
	except Exception as E:
		print("Exception occured:",E);



if __name__ == "__main__":
	main();
