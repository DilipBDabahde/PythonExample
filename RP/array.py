print("Demonstration of Array")

#there is no direct support for array in python we have to import array module to create array

import array as arr

# array module is imported as arr 

a = arr.array('i', [2,3,4,5]); # 'i' is considered as type code

print("first val is: ",a[3])

print(a.typecode)

print("before reverse: ",a);
a.reverse()

print("after reverse: ",a);

for i in range(len(a)):
	print(a[i])
	
b = arr.array('i',[1,2,1,2])

for i in range(len(b)):
	print(b[i])
	

i = 0

while(i < len(b)):
	print(b[i]);
	i = i + 1

print(type(b))


