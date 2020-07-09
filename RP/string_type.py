print("Demonstration of Strings")

name = 'Dilip Dabhade'
newname = 'Dinesh Dabhade'

print(name)
print(type(name))
print(newname)
print(type(newname))

print(name[0])
#print(name[20])

#negative index access element from right to left

print(name[-1])
print(name[-2])

# We can also print characters in range

print(name[0:4])
print(name[2:5])
print(name[2:])
print(name[:2])

print(name[0])


print(len(name))

address = "     house Num/19 Shekta village Tq: Paithan Dist: Aurangabad     "

print(address.strip())

#split method use to tokenize string

str1 = "PPA,LB,Python,LSP,Angular,Unix"
str1 = str1.split(',')

print(str1)
print(type(str1))
print(len(str1))

for i in range(0,len(str1)):
	print(str1[i])


