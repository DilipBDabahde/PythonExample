'''
Automation script which fetch URL from Wikipedia using Beautiful Soup.
'''

import os
import bs4
import requests
import sys


def linksDisplay(URK):
	
	res = requests.get(URK);
	print(type(res));

	soup = bs4.BeautifulSoup(res.text,'lxml');
	print(type(soup));

	links = soup.find_all('a',href = True);

	return links;

def main():
	print("Demonstration of WEBSCRAP")

	print("Application Name:",sys.argv[0]);

	if len(sys.argv)==2:

		if sys.argv[1]=="-h" or sys.argv[1]=="-H":
			print("This script is used to fetch links from Wikipedia file")
			exit();

		if sys.argv[1]=="-u" or sys.argv[1]=="-U":
			print("usage: ApplicationName");
			exit();

	url="https://en.wikipedia.org/wiki/Python_(programming_language)"

	arr = linksDisplay(url)

	for element in arr:
		if "#" not in element['href']:	
			print(element['href']);

if __name__ == "__main__":
	main();