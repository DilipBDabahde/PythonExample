'''
write python script which will help to send mail

accept userid from user		  		
accept userpassword from user  
accept receiver id from user

user_id = "abc1111@gmail.com";
user_pw = "weare@123"
receiver_id = "xyz@gmail.com"

'''

import sys
import urllib2
import time
import smtplib


def is_connected():
	
	try:
		urllib2.urlopen("http://216.58.192.142",timeout=1);
		return True;
	except urllib2.URLError as err:
		return False;
		
		

def MailSender(user_id, user_pw, receiver_id):
	
	sent_from = user_id;
	to = [receiver_id];
	email_text = "Welcome to Automailsending Process";
	
	try:
		server = smtplib.SMTP_SSL("smtp.gmail.com",465);
		server.ehlo();
		server.login(user_id, user_pw);
		server.sendmail(sent_from, to, email_text);
		server.close();
		
		print("Mail sent successfully...");		

	except Exception as E:
		print("Exception Occured",E);


def main():

	print("Application Name: ",sys.argv[0]);
	
	if len(sys.argv) != 4:
		print("Invalid input");
		print("input like .py  user_id  user_pw  receiver_id");
		exit();
		
	user_id = sys.argv[1];
	user_pw = sys.argv[2];
	receiver_id = sys.argv[3];
	
	try:		
		connected = is_connected();
	
		if connected:			
			print("connected");
			start_time = time.time();
			MailSender(user_id, user_pw, receiver_id);	
			end_time = time.time();
			
			print("Total %s seconds to send mail."%(end_time-start_time));
			
		else:
			print("There is no internet conntection...");

	except Exception as E:
		print("Exception Occured ",E)


if __name__ == "__main__":
	main();
