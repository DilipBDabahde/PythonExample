'''
Automation script which accepts time interval from user and create log file in that Marvellous directory which contains
information of all running processes. After creating the log file send that log file through mail.

write script which create periodic log file of RAM and send via gmail

'''
import sys 
import psutil
import schedule	
import time
import urllib2
import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

##################################################################################################################

def is_connected():	
	try:
		urllib2.urlopen("http://216.58.192.142",timeout=1);
		return True;
	except urllib2.URLError as err:
		return False;

##################################################################################################################

def MailSender(filename, time, user_id=sys.argv[2], user_pw=sys.argv[3], receiver_id=sys.argv[4]):
	try:
		msg = MIMEMultipart();
	
		msg['From']=user_id;
	
		msg['To']=receiver_id;
		
		body = """
		Hello %s,
		Welcome to Automailsending 
		please find attach document which contains logs of Running process.
		Log file is created at: %s
	
		This is auto generated mail.
		
		Thanks & Regards,
		Name:- First Middle Last
		""" %(receiver_id, time);
		
		Subject= """
		Running Processes log generated at : %s"""%(time)
		
		#
		msg['Subject']=Subject;
		
		msg.attach(MIMEText(body,'plain'));
		
		attachment = open(filename,'rb');
		
		p = MIMEBase('application','octet-stream');
		#
		p.set_payload((attachment).read());
			
		encoders.encode_base64(p);
		
		p.add_header('Content-Disposition',"attachment; filename=%s"% filename);
		
		msg.attach(p);
		
		s = smtplib.SMTP_SSL("smtp.gmail.com",465);
	
		s.ehlo();	
	
		s.login(user_id,user_pw);
		
		text = msg.as_string();
		
		s.sendmail(user_id, receiver_id, text);
	
		s.quit();
		
		print("Log file successfully sent through Mail");
	
	except Exception as E:
		print("Exception occured",E);
		
##################################################################################################################

def ProcessLog(log_dir = "Logger"):
	print("Inside Processlog1")
		
	if not os.path.exists(log_dir):
		os.mkdir(log_dir);
	
	seperator= ("-"*80);
	log_path = os.path.join(log_dir,"Logfile %s.txt"%time.ctime());
	fobj = open(log_path,'w');
	fobj.write(seperator+"\n")	
	fobj.write("Process Running on RAM Logger Report "+time.ctime()+"\n")	
	fobj.write(seperator+"\n")	

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username']);
			fobj.write(str(pinfo));
			fobj.write("\n");
			
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass		
	
	fobj.close();	
	print("Inside Processlog7")
	print("Logfile is successfully generated at location %s"%log_path);


	connected = is_connected();
	
	if connected:
		print("Inside Processlog8")
		starttime = time.time();
		MailSender(log_path,time.ctime());
		endtime = time.time();
		
		print("Time took %s seconds"%(endtime - starttime));
		
	else:
		print("No internet connection....");	

##################################################################################################################	

def main():
	
	print("Application Name: ",sys.argv[0]);
	
	if len(sys.argv) != 5 :
		print("Invalid input");
		print("input like  .py  TimeInMinutes  user_id  user_pw  receiver");
		exit();			
	
	try:
		schedule.every(int(str(sys.argv[1]))).minutes.do(ProcessLog);
	
		while(1):
			schedule.run_pending();
			time.sleep(1);
			
	except Exception as E:
		print("Exception occured", E);

##################################################################################################################

if __name__ == "__main__":
	main();
