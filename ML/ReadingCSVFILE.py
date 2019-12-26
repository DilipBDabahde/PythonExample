import pandas as pd

'''
we are using pandas to read .csv file

in this program we are going to read csv file data with help of pandas labrary
'''

class ReadFile:
	
	
	def i_am_reading_csvfile(path):
		
		i_red_file_data = pd.read_csv(path);
		print(i_red_file_data);


def main():

	path = input("Enter path");

	obj = ReadFile;

	try:

		obj.i_am_reading_csvfile(path);

	except Exception as e:
		print("Exception occured : ",e);


if __name__ == "__main__":
		main();
