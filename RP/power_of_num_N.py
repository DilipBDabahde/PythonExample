'''
wap which accept two number  , first to make use num and second to make first number power with a targeted num

input: 5	4		for 5 number we have to generate power of 4  like  5*5*5*5
output: 625

'''



fp = lambda no,power : no ** power;


num = int(input("Enter a Number: "));
power = int(input("Enter power number: "));

total = fp(num, power);

print(total);


