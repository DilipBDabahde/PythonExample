'''
accept N values from user and display them in list
input: 5
ouput: 3 2 5 9 2
'''

#create empty list

arr = list();	#list created

num = input("Enter size of list: ");

print("Enter values as given size");

for i in range(0,int(num)):
	no = input("Val:");
	arr.append(int(no));

print("Our list is:",arr)
