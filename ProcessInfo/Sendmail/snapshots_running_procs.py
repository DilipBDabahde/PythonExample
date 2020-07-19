'''
4. Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.
Usage : ProcInfoLog.py Demo goodmorning@gmail.com
Demo is name of Directory.
goodmorning@gmail.com is gmail id

input shoult like: python3 file.py Dirname sender_id sernder_pw receiver_id

'''

from sys import *;
import os
import time, psutil
from urllib.request import urlopen # this is used to check internet
#need to import mail sending modules

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase





def is_connected():
	try:
		urlopen("https://www.google.com/", timeout = 10);
		return True;
	except:
		return False;
		
def MailSender(path, timer):
	
	try:
		sender_id = argv[2];
		receiver_id = argv[4];
		sender_pw = argv[3]; #accept these all from user through terminal
		
		msg = MIMEMultipart(); # MIMEMultipart class object is created

		msg['From'] = sender_id;
		msg['To'] = receiver_id;

		body = """
			Hello %s,
			तुमचे स्वागत आहे ह्या mail  मध्ये आपल्या मेमरी मध्ये run  होणाऱ्या process चा स्नॅपशॉट घेऊन त्याची file सेंट केली आहे . ती file तपासून घ्या 
			Logfile is create at: %s
			हा ऑटो जनरेटेड  mail  आहे ,
			"""%(receiver_id, timer);
		msg['Subject'] = """Running  Processes snapshot created at  :%s"""%timer;		
		msg.attach(MIMEText(body, 'plain'));
				
		attachment = open(path, 'rb'); #opening file in rb mode
		p = MIMEBase('application', 'octet-stream');
		p.set_payload((attachment).read());
		encoders.encode_base64(p);		
		p.add_header('Content-Disposition',"attachment; filename= %s"%path);
		msg.attach(p);

		
		smtpobj = smtplib.SMTP('smtp.gmail.com',587);
		smtpobj.starttls(); #starttls();		ehlo
		smtpobj.login(sender_id, sender_pw);
		text = msg.as_string();
		smtpobj.sendmail(sender_id, receiver_id, text);
		smtpobj.quit();
		
		print("Logfile successfully sent through Mail");
	except Exception as e:
		print("Unable to send mail: ",e);
		

def Snapshots_of_running_procs():
	dirname = argv[1];
	sender_id = argv[2];
	
	if not os.path.exists(dirname):
		os.makedirs(dirname);

	dirname =os.path.abspath(dirname);
	
	if os.path.isdir(dirname):
		filename = "Logfile%s.text"%(time.ctime());

		filename = os.path.join(dirname, filename)		

		fd = open(filename, 'w');
		fd.write("-"*70+"\n");
		fd.write(filename+"\n")
		fd.write("This file contains all runninng processes snapshots of memory\n");
		fd.write("-"*70+"\n");
		icnt = 0;
		for proc in psutil.process_iter():
			fd.write(str(proc.as_dict(attrs=['pid','name','username']))+"\n");
			icnt = icnt + 1;
		fd.write("Total running processes are : "+str(icnt)+"\n");		
		fd.close();
		print("Logfile is created successfully");
		
		
		if is_connected(): # this statement is used to check internet connectedion
			starttime = time.time();

			MailSender(filename, time.ctime())
			endtime = time.time();
			print("Required time to sent mail is: %s"%(endtime - starttime));
		else:
			print("There is no internet connection");			
	
	
		
			
	
	
def usage():
	print("Usage: This application is used to take snapshots of running processes of memory and send mail");


def help():
	print("to run this script need input like: python3 file.py demo goodmorning@gmail.com\nthen we can use this script");


def main():
	print("Application name: ",argv[0]);
	print("Enter -h or -H for help");
	print("Enter -u or -U for knowing usage");

	if argv[1] == '-h' or argv[1] == '-H':
		help();
		exit();
	
	if argv[1] == '-u' or argv[1] == '-U':
		usage();
		exit();
	
	if len(argv) != 5:
		print("invalid input arguments");
		exit();
	
	try:	
		Snapshots_of_running_procs();
		
	
	except Exception as e:
		print("Exception occured "+e);
		
		
if __name__ == "__main__":
	main();
