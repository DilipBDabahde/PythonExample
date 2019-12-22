'''
in this demo application we are using inbuild dataset of iris to get start for learn ML 
and in this demo we are just printing total features names and target names using loop

to load iris datasets we are going to use sklearn library which contains iris datasets in it by using this library we are trying to execute its flow

'''

from sklearn.datasets import load_iris


iris = load_iris();

print(iris);
print("-"*68)
print("Featurse names of iris data set");
print(iris.feature_names);
print("-"*68)

print("Targets of name of iris datasets");
print(iris.target_names);
print("-"*68)

print("First 10 elements from iris data set");

for i in range(len(iris.target)):
	print("{ ID: %d }:{Label %s}:{Feature : %s}"%(i,iris.data[i],iris.target[i]));

