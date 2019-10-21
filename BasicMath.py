'''
define basic maths function where we can send 2 val and get back its output using +,-,*,/

input: 5 2   use +  output:7
	     use -  output:3
	     use *  output:10
	     use // output:2

'''


def Add(no1, no2):
	ans = no1 + no2;
	return ans;

def Sub(no1, no2):
	ans = no1 - no2;
	return ans;

def Multi(no1, no2):
	ans = no1 * no2;
	return ans;

def Div(no1, no2):
	ans = no1 // no2;
	return ans;
	
	
import sys;
def main():
  
   iNo1 = int(sys.argv[1]); #arg 1
   iNo2 = int(sys.argv[2]); #arg 2
 
   result = Add(iNo1, iNo2);
   print("Addition of two nums is :",result);
   
   result = Sub(iNo1, iNo2);
   print("Subtraction of two num is :",result);
   
   result = Multi(iNo1, iNo2);
   print("Multi of Two nums is :",result);
   
   result = Div(iNo1, iNo2);
   print("Division of Two nums is :",result);
   
   

if __name__ == '__main__':
	main();
