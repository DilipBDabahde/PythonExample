from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree


print("show path from where tree comes: ",tree);

irisdata = load_iris(); # load irisdata set

print("-"*66)
print("Features names of iris datassest")
print(irisdata.feature_names);

print("-"*66);
print("Target names of iris datasets");
print(irisdata.target_names);


#indices of removed elements

test_index = [1, 51, 100];

#Training data with remove data
print("-"*66);
print("We got this after rm test_index of target");
train_target = np.delete(irisdata.target, test_index);
print(train_target);

print("-"*66);
print("We got this after we remove features of test_index");
train_data = np.delete(irisdata.data, test_index,axis = 0);
print(train_data);
print("-"*66);


#testing data for testing on training data
print("Target for test")
test_target = irisdata.target[test_index];
print(test_target);
print("-"*66)


print("Data rm from given index")
test_data = irisdata.data[test_index];
print(test_data);
print("-"*66);

#from decision tree classifier

classifier = tree.DecisionTreeClassifier();
print(classifier)
'''
DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',
                       max_depth=None, max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, presort='deprecated',
                       random_state=None, splitter='best')
'''

#Apply training data to form tree
classifier.fit(train_data, train_target);

print("Values that we removed for testing");
print(test_target);

print("Result of testing");
print(classifier.predict(test_data));

#visualization
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(classifier, out_file = dot_data, feature_names=irisdata.feature_names, class_names=irisdata.target_names, filled=True, rounded = True, impurity = False);

graph = pydot.graph_from_dot_data(dot_data.getvalue());

graph[0].write_pdf("irisData.pdf");
