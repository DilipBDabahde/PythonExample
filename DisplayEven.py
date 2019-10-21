# accept one num as command line argument and display till that num even values

def DisEven(no)                   # (step3) then loop extecute till cond is true after 
	for i in range(1,no):     # all execution control go back from  where it came
		if i % 2 == 0:
			print(i);
			
			
import sys;
def main():			# (step2) control go inside this definition then argv val stores into no then line 12 fun call
	no = int(sys.argv[1]);  # from 12 control go to line num 3 
	DisEven(no);		# call to DisEven(no)
	
if __name__ =='__main__':       # first control come on line 14 if cond it true then call main() fun definition (step1)
	main();
