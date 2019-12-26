'''
useing knn and decisiontree for irisdata set to check their accuracy
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


class CheckAccuracy:

	def __init__(self):
		pass

	def UseDecisionTree():
		#step 1  gathering data
		iris = load_iris();

		#seperating data
		#step2 cleaning data
		data = iris.data; 	
		target = iris.target;

		data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

		#step 3 fixing algo
		classifier = tree.DecisionTreeClassifier();

		#step 4 trainign data
		classifier.fit(data_train, target_train);

		#step 5 testing
		predictions = classifier.predict(data_test);

		Accuracy = accuracy_score(target_test, predictions);

		return Accuracy;

	def UseKNN():

		#step 1 loading dataset or gathering data
		iris = load_iris();

		#step2 cleaning and preparing data
		data = iris.data;
		target = iris.target;

		data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5);

		#step3 analysis of algo
		KNN = KNeighborsClassifier();

		#step4 traing data
		KNN.fit(data_train, target_train);

		#step5 testing 
		predictions = KNN.predict(data_test);

		Accuracy = accuracy_score(target_test, predictions);
		return Accuracy;


def main():

	obj = CheckAccuracy;
	Accuracy = obj.UseDecisionTree();
	print("Accuracy of decisiontree is: ",Accuracy*100,"%");

	Accuracy = obj.UseKNN();
	print("Accuracy of KNN is: ",Accuracy*100,"%");


if __name__ == "__main__":
	main();