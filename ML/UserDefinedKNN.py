"""
user defined KNN ALGO

classifier: User Defined K Nearest Neighbour
Dataset : 	Iris DataSet
Features 	Sepel with,Sepal length, petal width petal length

Labels:		Versicolr, setosa, Verginica
Training Dataset:	75Entries
Testing Dataset: 	75Entries
"""

from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def euc(a,b):

	return distance.euclidean(a,b);


class MarvellousKNN():
	def fit(self, TrainingData, TrainingTarget):
		self.TrainingData = TrainingData
		self.TrainingTarget = TrainingTarget
		
	def predict(self, TestData):
		predictions = []
		for row in TestData:
			label = self.closest(row);
			predictions.append(label);
		
		return predictions

	def closest(self, row):
		bestDistance = euc(row,self.TrainingData[0]);
		print(bestDistance);
		
		for i in range(1,len(self.TrainingData)):
			dist= euc(row, self.TrainingData[i]);
			if dist < bestDistance:
				bestDistance = dist;
				bestIndex = i;
		return self.TrainingTarget[bestIndex];
			
	
def MarvellousKNeighbor():
	border = "-"*77;
	
	iris = load_iris(); # data loaded
	
	data = iris.data;
	target = iris.target;
	
	print(border);
	print("Actual data set");
	print(border);
	
	for i in range(len(iris.target)):
		print("ID: %d, Feature %s Label %s"%(i,iris.data[i],iris.target[i]))
	
	print("Size of actual data set %d"%(i+1));
	
	data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5); # here we divide all data into 50 50 format 
	
	
	print(border);
	print("Training data set")
	print(border);
	
	for i in range(len(data_train)):
		print("ID: %d, Label %s, Features: %s"%	(i,data_train[i],target_train[i]));
	
	print("size of traing data set:%d"%(i+1))
	
	
	print(border);
	print("Test data set");
	print(border);
	
	for i in range(len(data_test)):
		print("ID: %d, Label %s, Features: %s"%(i,data_test[i],target_test[i]));
		
	print("size of test data set %d"%(i+1));
	print(border);
	
	
	classifier = MarvellousKNN(); # mknn obj creataed
	classifier.fit(data_train,target_train); # call to fit with dataset
	predictions = classifier.predict(data_test); # prediction our datatest 
	Accuracy = accuracy_score(target_test, predictions);
	return Accuracy;
	

def main():
	Accuracy = MarvellousKNeighbor();
	print("Accuracy of classification algo with K neighbor classify is ",Accuracy*100,"%");	
	

if __name__ == "__main__":
	main();
