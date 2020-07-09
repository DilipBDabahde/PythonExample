#using Filter, Map, Reduce with user define function instead of lambda

def evenChk(no):
	return (no % 2 == 0);


def increase(no):
	return no + 2;


def add(a, b):
	return a + b;

#created list with some elements
arr = [8,9,5,16,2,4,21,30,11]


#using filter with user define function
evenArr = list(filter(evenChk, arr))
print("Data after filter: ",evenArr);



# using map with user define function

modArr = list(map(increase, evenArr));
print("now our data is modified here:",modArr);


# using reduce with user define function
import functools

sum = functools.reduce(add, modArr);
print("Addition is :",sum);


