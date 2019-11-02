#use of lambda expresssion 

lam = lambda a,b:a+b;

res = lam(11,44)

print(res)

#now check use of Map,reduce,filte fuction

#use of filter with lambda

arr = [5,13,53,26,65,2436,73,25,472,54,457,253]

faa = list(filter(lambda no:(no%2==0),arr))

print(faa); # this line will print evenonly



#use of map with lambda

sum = list(map(lambda no:(no+2),faa));
print(sum);


#use of reduce with lambda
#need to import reduce funct from fucttools
#here we have all sum of all list
from functools import reduce

redfun = reduce(lambda no1,no2:no1+no2,sum);

print(redfun);
