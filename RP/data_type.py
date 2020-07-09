print("Demo of Data types in python")

no = None
print(no)
print(type(no))
print(id(no))

print("-"*80)
no = 11
print(no)
print(type(no))
print(id(no))

print("-"*80)
print("Numeric datatype contains diffrent sub types as int,float,bool,complex")

no = 11 # int
print(type(no))

no = 3.14  # float
print(type(no));

no = 6 + 3j  # complex value
print(type(no))

no = True  # boolean
print(type(no))
print("-"*80)


print("converting type of variable")

no  = 11
print(no)
print(type(no));
print(id(no))

no = float(no)
print(no)
print(type(no));
print(id(no))
print("-"*80)

a = 5
b = 8
no = complex(a,b)
print(no)
print(type(no))
print(id(no))

print("-"*80)
print("Under Sequence there are different data types as List,Set,Tuple, Range");

# creating list
alist = [12,22,44,55]
print(alist)
print(type(alist))
print(id(alist))
print("")

#creating set
aset = {12,53,53,56,343}
print(aset)
print(type(aset))
print(id(aset))
print("")

#creating tuple
atuple = (12,462,55,23,5)
print(atuple)
print(type(atuple))
print(id(atuple))
print("")

#creating String
name = "Dilip Dabhade"
print(name)
print(type(name))
print(id(name))
print("")

#demo of range using list

for i in range(1,10):  #default start from 0
	print(i);
	
print("")
	
for i in range(1,10,2): # jump by 2 eachtime
	print(i);

print("")


# Dictionary which has key and values
#batches is dict name

batches = {'PPA':9000,'LB':7500,'Python':6500,'LSP':11000};

print(batches)
print(type(batches))
print(batches.keys())
print(batches.values())
print(batches['LB']) # 7500
print(batches['Python']) # 6500
print("")
