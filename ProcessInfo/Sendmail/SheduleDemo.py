
import schedule,time

def fun(fname, mname, lname):
	
	print(fname, mname, lname);
	print("hello")




def main():
	a = 30
	b = 20
	c = 10
	schedule.every(5).seconds.do(fun, a, b, c);
	
	while 1:
		schedule.run_pending();
		time.sleep(1);


if __name__ == "__main__":
	main();
