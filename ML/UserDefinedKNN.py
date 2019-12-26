
"""
user defined knn
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import sys
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

def euc(x, y):
	return distance.euclidean(x, y);


class UserDefinedKNN:

	def fit(self,data_x, target_x):
		self.data_x = data_x;
		self.target_x = target_x;
	
	def predict(self, data_y):
		prediction = [];

		for row in data_y:
			label = self.closest(row);
			prediction.append(label);
		return prediction;

	def closest(self, row):
		basedistance = euc(row, self.data_x[0]);
		best_index = 0;
		for i in range(1, len(self.data_x)):
			dist = euc(row, self.data_x[i]);
			if dist < basedistance:
				basedistance = dist;
				best_index = i;

		return self.target_x[best_index];


def RenewKNN():

	iris = load_iris(); #step1 gathering data

	data = iris.data;	# step2 cleaning dataset
	target =iris.target;
	data_x, data_y, target_x, target_y = train_test_split(data, target, test_size=0.5);


	clf = UserDefinedKNN();	# step3 fix algo

	clf.fit(data_x, target_x);	# step4 training 

	predict = clf.predict(data_y);
	print(predict);

	Accuracy = accuracy_score(target_y, predict);

	return Accuracy;

def main():

	print("Application Name: ",sys.argv[0]);

	try:

		Accuracy = RenewKNN();
		print("Accuracy is :",Accuracy*100,"%");
	except Exception as e:
		print("Exception occured: ",e);


if __name__ =="__main__":
	main();