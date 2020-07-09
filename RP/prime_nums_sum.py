'''
write a program which accpet N nums from user in list and make addition of Prime nums of list

input: Num of elements : 12
input Elements: 5  8  6  8  5  9  3  7  2  21  11  5

output: Sum of all prime num is:  38

'''


def check_Prime(no):
	
	icnt = 0;
	
	for i in range(2, (no+1)//2):
		if no % i == 0:
			icnt = icnt + 1;
	
	if icnt > 0:
		return False;
	else:
		return True;


def addition_prime(arr):
	
	if len(arr) < 0:
		return -1;
	
	isum = 0;
	prime_list = list();
	
	for i in range(0, len(arr)):		
		result = check_Prime(arr[i]); # calling to check_Prime if it is True return True, then add to isum
		if result == True:
			isum = isum + arr[i];
			prime_list.append(arr[i]);
	
	print("Primes are: ",prime_list);
	return isum;	# after getting all prime we return them to caller


def main():
	
	list_arr = list(); # list class object is created
	size  = input("Enter element size: ");
	size = int(size); # type conversion
	
	for i in range(0,size):
		no = input("Enter element: ");
		no = int(no); # type conversion
		list_arr.append(no);  # appending elements into list
	
	print("List is created now: ", list_arr);
	result = addition_prime(list_arr);
	
	print("Sum of all prime nums of list: ", result);

if __name__ == "__main__":
	main();
	
	
