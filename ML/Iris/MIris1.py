import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris


irisdata = load_iris() # loading irisdatasets

print(irisdata);
print("All dataset is loaded sucessfully");

print("-"*66)
print("Features names of iris dataset");
print(irisdata.feature_names);	
print("We got our features names for irisdata");

print("-"*66);
print("Target names of dataset")
print(irisdata.target_names);
print("We got taget names ");
print("-"*66);

#indices removed elements for testing 
test_index = [1,51,100];

#training data with removed elements
train_target = np.delete(irisdata.target, test_index); 
print(train_target);
print("-"*66);

train_data = np.delete(irisdata.data, test_index, axis=0);
print(train_data);
print("-"*66) # index rm


#testing data for testing on training data
test_target = irisdata.target[test_index];
print("This is target for testing")
print(test_target); # this is dream to find
print("-"*66);

print("Rm featurs of perticular index");
test_data = irisdata.data[test_index];
print(test_data); 
print("-"*66);


#from dicision tree classifier

classifier = tree.DecisionTreeClassifier();

#apply training data to form tree
classifier.fit(train_data, train_target);


print("Values that we removed for testing");
print(test_target);
print("-"*66);

print("Result of tesing");
print(classifier.predict(test_data));
