'''
4. Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.

input:

Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id.
'''

import sys
import os
import urllib2
import time
import psutil
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

	
def is_connected():

	try:
		urllib2.urlopen("http://216.58.192.142",timeout=5);
		return True;

	except urllib2.URLError as err:
		return False;
###########################################################################################

def MailSender(filename):
	
	try:
		Senderid = sys.argv[2];	# From
		Senderpw = sys.argv[3];
		Receiverid = sys.argv[4]; # To


		msg = MIMEMultipart();
		msg['From']= Senderid;
		msg['To'] = Receiverid;
		
		body = """
		Hello %s,
		Welcome to Automailsending 
		please check attach document which contains logs of Running process.
		Log file is attached
	
		This is auto generated mail.
		
		Thanks & Regards,
		Name:- First Middle Last
		""" %(Receiverid);

		Subject = """
		Logfile of Running Process on machine """
		print("Sending Mail....")

		msg['Subject'] = Subject;
		
		msg.attach(MIMEText(body, 'plain'))
		attachment = open(filename,'rb');

		p = MIMEBase('application','octet-stream')
		
		p.set_payload((attachment).read());
		encoders.encode_base64(p);

		p.add_header('Content-Disposition',"attachment; filename=%s"%filename);
		
		msg.attach(p);

		server = smtplib.SMTP_SSL("smtp.gmail.com",465);

		server.ehlo();
		server.login(Senderid,Senderpw);

		text = msg.as_string();

		server.sendmail(Senderid,Receiverid,text);
		server.quit();

		print("Log file Successfully sent via gmail");	

	except Exception as E:
		print("Exception occured",E);




###########################################################################################

def process_bio(Dirname):
	
	if not os.path.exists(Dirname):
		os.makedirs(Dirname);

	filename = "Logfile%s.txt"%time.ctime();
	filename = os.path.join(Dirname, filename);
	
	fobj = open(filename,'w');
	seperator = "-"*80+"\n";   
	fobj.write(seperator);
	fobj.write("Running Process Statistics %s"%time.ctime());
	fobj.write("\n"+seperator);

	for proc in psutil.process_iter(attrs=["username",'name','pid']):
		fobj.write(str(proc.info));
		fobj.write("\n");

	fobj.close();
	print("Successfully created logfile");

	connected = is_connected();

	if connected:			
		starttime = time.time();
		MailSender(filename);
		endtime = time.time();

		print("Total took time is: %s"%(endtime - starttime));

	else:
		print("you do not have internet connection ....")
###########################################################################################

def main():

	print("Application Name:",sys.argv[0])

	if len(sys.argv) != 3:
		print("Invalid input");
		print("Input like: .py	DirName	email-id"); 

	try:
		process_bio(sys.argv[1])

	except Exception as E:
			print("Exception occured",E);

###########################################################################################

if __name__ == "__main__":
	main();