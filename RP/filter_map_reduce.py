# Filter Map Reduce implementation


#creating list

arr = [8,9,5,16,2,4,21,30,11]

print("Our list is: ",arr);

#syntax for filter
#list(function_to_apply, list_of_inputs)

evenArr = list(filter(lambda no : (no % 2 ==0 ), arr))

#here above we used lambda in filter to get even list

print("Our evenlist is: ",evenArr);

#######################################################
#map usage

ModArray = list(map(lambda no : no + 2, evenArr));

print("After modified evenArray: ",ModArray);
# here above we modified our array with value two

#######################################################
#reduce usage 
# this inbuit function is used to reduce large data
#syntax reduce(function_to_apply, list_of_inputs)
# to use REDUCE inbuit function we need to import a module "functools"

import functools 

sum = functools.reduce( lambda a,b : a+b, ModArray)

print("reduce created sum: ",sum);

#by using reduce function we get targeted output where we reach on expected op.
# to get access for reduce we need to append REDUCE fun with functools.reduce likewise as above used

