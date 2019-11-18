'''
use of 
open()
close()
write()
calls

'''
import sys
from sys import *


fobj = open("/home/dilip/ttmm.txt",'w');	# this 'w' value is used to create new file 

#print(fobj.read());					# we try to print value of ttmm.txt but it is empty

fobj.close(); # we close the created file and it's obj

#print(fobj.read());

fobj = open("/home/dilip/ttmm.txt",'a'); # we again open file to append text into 
fobj.write("hello this is DILIP. ");	# nnow we add string into the file
fobj.close();							# after our work done we close the file obj


fobj = open("/home/dilip/ttmm.txt",'r');  # we again open file to check string is added or not into file
print(fobj.read());			# print added string 
fobj.close();		# we have to close that file to reopen if we req


fobj = open("/home/dilip/ttmm.txt",'w+a');
fobj.write(" Welcome to NewYork\n");
fobj.close();
''
fobj = open("/home/dilip/ttmm.txt",'r');
print(fobj.read());
fobj.close();
