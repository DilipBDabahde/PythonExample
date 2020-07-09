print("Demonstration of Set")

set_type = {12,'Dilip',3.14,'Rama',89}

print(set_type)
print(len(set_type))
set_type.remove(12)
print(set_type)
set_type.discard('Dilip')
print(set_type)

#add new element in set type

set_type.add('Dipak')
print(set_type)
