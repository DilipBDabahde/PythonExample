import pandas as pd

'''
we are using pandas to read .excel file
'''

class ReadFile:
	
	
	def i_am_reading_Excelfile(path):
		
		i_red_file_data = pd.read_excel(path);
		print(i_red_file_data);


def main():

	path = input("Enter path");

	obj = ReadFile;

	try:

		obj.i_am_reading_Excelfile(path);

	except Exception as e:
		print("Exception occured : ",e);


if __name__ == "__main__":
		main();
