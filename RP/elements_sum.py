'''
Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

input: Num of Elements : 4
input Elements: 12 5  6 7 
output: 30
'''


arr = list(); #created empty list

size = input("Enter element size: ");

size = int(size); #type conversion

print("Enter elements: ");

for i in range(0,size):			# loop iterating to take input from user
	value = input("Enter element: ");
	value = int(value);
	arr.append(value); #adding element into list


#created list
print("All elements of list: ",arr);

#making addition of all elements

isum = 0;
for i in range(0,size):		# loop iterating to make sum of all elements
	isum = isum + arr[i];


print("Sum of all elements is:" ,isum)
