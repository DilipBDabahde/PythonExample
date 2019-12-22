'''
in this application we are using KNN and Decision Tree algo to find accuracy of our application

Note : Accuracy may vary.
'''

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def Cal_Accu_Of_DecisionTree():
	iris =  load_iris();
	
	data = iris.data;
	target = iris.target;	

	data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5);
	
	classifier = tree.DecisionTreeClassifier();
	classifier.fit(data_train, target_train);
	
	predictions = classifier.predict(data_test);
	
	Accuracy = accuracy_score(target_test, predictions);
	return Accuracy;


def Cal_Accu_Of_KNN():
	iris = load_iris();
	
	data = iris.data;
	target= iris.target;

	data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5);
	
	classifier = KNeighborsClassifier();
	classifier.fit(data_train, target_train);
	predictions = classifier.predict(data_test);
	Accuracy = accuracy_score(target_test, predictions);
	return Accuracy;
	


def main():
	Accuracy = Cal_Accu_Of_DecisionTree();
	
	print("Accuracy of clssification algoriths with decision tree classifier is",Accuracy*100,"%");
	
	Accuracy = Cal_Accu_Of_KNN();
	print("Accuracy of Classification algorithms with k Neighbor classifier is", Accuracy*100,"%");



if __name__ == "__main__":
	main();
