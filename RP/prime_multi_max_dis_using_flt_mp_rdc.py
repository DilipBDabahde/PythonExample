'''
.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).

Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

'''



def filter_prime(no):
	
	icnt = 0;
	
	for i in range(2, (no+1)//2):
		if no % i == 0:
			icnt = icnt + 1;
		
	if icnt > 0:
		return False;
	else:	
		return True;


def map_mult_by2(no):
	return no*2;


def reduce_max(no1, no2):
	if no1 >= no2:
		return no1;
	else:
		return no2;
	


def main():
	
	arr_list = list();
	
	size = int(input("Enter size of list :"));
	
	print("Enter elements for array: ");
	for i in range(0,size):
		arr_list.append(int(input("Enter element:")));
	
	if len(arr_list) > 0:
		
		print("List is created successfully");
		
		prime_list = list(filter(filter_prime, arr_list));
		print("all primes are :",prime_list);
		
		if len(prime_list) > 0:
			prime_multi = list(map(map_mult_by2, prime_list));
			print("Each prime num is multi by 2:", prime_multi);
			
		import functools
		if len(prime_multi) > 0:
			imax = functools.reduce(reduce_max, prime_multi);
		
		print("max num from mapped list is:", imax);	
			
	else:
		print("empty list:");
		
if __name__ == "__main__":
	main();
	
	
