'''
Consider below python application which schedule task after Minute, Hour as well as on specific Day or specific time.
'''

import schedule
import time
import datetime 


def fun_Minute():
	print("Current time is")
	print(datetime.datetime.now());
	print("Schedular executed after Minute");

def fun_Hour():
	print("Current time is")
	print(datetime.datetime.now());
	print("Schedular executed after Hour");
	
def fun_Day():
	print("Current time is")
	print(datetime.datetime.now());
	print("Schedular executed after Day");
	
def fun_Afternoon():
	print("Current time is")
	print(datetime.datetime.now());
	print("Schedular executed at 12");


def main():
	print("Demonstration of Automation and Machine Learning");
	
	print("Python Job Schedular");
	print(datetime.datetime.now());
	
	schedule.every(1).minutes.do(fun_Minute);
	
	schedule.every().hour.do(fun_Hour);
	
	schedule.every().day.at("00:00").do(fun_Afternoon);
	
	schedule.every().sunday.do(fun_Day);
	
	schedule.every().saturday.at("18:30").do(fun_Day);
	
	while True:
		schedule.run_pending();
		time.sleep(1);

if __name__ == "__main__":
	main();
