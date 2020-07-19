from sys import *
import os
#to hash message
import hashlib

#time relatated activities
import time
#to make scheduling 
import schedule

#to send mail
import smtplib

#to compose mail
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#to open web for net checking
from urllib.request import urlopen 

################################################################################################
def is_connected():
	try:
		urlopen('https://www.google.com', timeout = 10);
		return True;
	except:
		return False;

################################################################################################
def help():
	print("This script required input: python3 DupFiles_Search_MKLogFile_SendMail.py Demo Temp2 int(time_in_minutes) sender_id sender_pw receiver_id");

################################################################################################

def usage():
	print("Usage: This script is used to find all duplicates files of given dir\nAnd delete all duplicate files and make logfile of that duplicate files\nAfter that send mail of this logfile.");
################################################################################################


def hasher(path):
	fd = open(path, 'rb');
	data = fd.read();
	fd.close();
	return hashlib.md5(data).hexdigest();

################################################################################################

def DeleteDups(path, dirname,):
	orglist = [];
	duplist = [];
	
	if not os.path.exists(path):
		print(path+": This dir is not existing");
		exit();
	else:
		path = os.path.abspath(path);
		
	if not os.path.exists(dirname):
		os.makedirs(dirname);

	
	filename = "Logfile%s.text"%time.ctime();
	filepath = os.path.join(os.path.abspath(dirname), filename);

	fd = open(filepath, 'w');
	fd.write("-"*70+'\n');
	fd.write("This is log File of all duplicates files\n");
	fd.write("%s \n"%filename);
	fd.write("-"*70+'\n');
	fd.write("-"*70+'\n');
	
	icnt = 0
	
	for folder, subfolder, files in os.walk(path):
		for fname in files:
			fullname = os.path.join(folder, fname)
			checksum = hasher(fullname);
			
			if len(orglist) == 0:
				orglist.append(checksum);
			else:
				if not checksum  in orglist:
					orglist.append(checksum);
				else:
					fd.write(fname+"\n");
					os.remove(fullname);
					icnt = icnt + 1;
	fd.write("-"*70+'\n');
	fd.write("-"*70+'\n');
	fd.write("Total duplicates files are: "+str(icnt)+"\n");
	fd.write("-"*70+'\n');
	fd.close();
	print("Logfile is created successfully of dups files");
	
	if is_connected():
		print("its connected");
		MailSender(filepath, time.ctime());
	else:
		print("There is no internet connection");
		exit();
################################################################################################

def MailSender(path, timer):
	print(path)
	print(timer)
	sender_id = argv[4];
	sender_pw = argv[5];
	receiver_id = argv[6];
	
	try:
		#mail conposition start
		msg = MIMEMultipart(); # msg is object of MIMEMultipart
		
		msg['From']	= sender_id;
		msg['To'] = receiver_id;
		
		body = """
			🙏️नमस्कार 🙏️ %s
			खाली असलेल्या file  मध्ये Duplicates  फाइल्स ची यादी आहे. जे कि आपल्याला दिलेल्या फोल्डर मधून बनवली आहे . पण हि यादी बनावत असताना duplicates फाइल्स काढून टाकल्या आणि त्या duplicates फाइल्स ची नोंद इथे केली आहे  ."""%receiver_id;
			
		msg ['Subject'] = """Duplicate files remover script result created at: %s"""%timer;
		
		msg.attach(MIMEText(body, 'plain'));
		
		attachment = open(path, 'rb');
		p = MIMEBase('application', 'octet-stream'); # p is object of mimebase class
		p.set_payload((attachment).read())
		encoders.encode_base64(p);
		p.add_header('Content-Disposition',"attachment; filename= %s"%path);
		msg.attach(p);
		#mail conposition end
		
		#mail sending started
		smtpobj = smtplib.SMTP('smtp.gmail.com', 587);
		smtpobj.starttls();
		smtpobj.login(sender_id, sender_pw)
		text = msg.as_string();
		smtpobj.sendmail(sender_id, receiver_id, text);
		smtpobj.quit();
		print("Logfile of duplicates files is sent successfully");
		
	except Exception as e:
		print("Unable to send mail: ",e);
	
	
	

