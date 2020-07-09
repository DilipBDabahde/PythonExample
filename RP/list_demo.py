print("Demonstration of List")

batches = ['PPA','LB','Angular','Python']

print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

#we can store hetrogeniousdata
data1 = [11, "Diwali",3.14]
print(data1)


data2 = [21,'Dasara',5.33]
print(data2)

combo = [data1, data2]
print(combo)

batches.append('MEAN')
print(batches)

batches.insert(2,"LSP")
print(batches)


batches.remove("LSP")
print(batches)

batches.pop()
print(batches)

batches.pop(2)
print(batches)

del batches[1:]
print(batches);

batches.extend(['LB','Python','Angular','MEAN'])
print(batches)

batches.sort()
print(batches)
