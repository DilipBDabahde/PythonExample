from sklearn import tree

'''
balls  Tennis   Cricket
Features Weights Surface

Weight = 1
Surface = 2

Tennis = 4
Cricket = 5

Tennis = Weight    from 30gm  to 60    
Cricket = Weight   from 90  to 150

ask user for Ball Weight and its Surface

Dataset
							 |----Surface   Rough = 1  & Smooth = 2
Weigth   Surface Labels		Sr   Lb -->Labels	Tennis = 1 & Cricket = 2  

45		 Rough	 Tennis		1    1
98		 Smooth  Cricket	2	 2
35		 Rough	 Tennis	    1	 1
67		 Smooth  Cricket	2	 2
88		 Smooth  Cricket	2 	 2
144		 Smooth  Cricket	2 	 2
35		 Rough	 Tennis		1	 1
47		 Rough	 Tennis		1	 1
132		 Smooth  Cricket	2	 2
39		 Rough	 Tennis		1	 2


'''


def MLTry(weight, surface):	# input       111 2    output: Cricket
	
	BallsFeatures = [[45,1],[98,2],[35,1],[67,2],[88,2],[144,2],[35,1],[47,1],[132,2],[39,1]];

	LabelsSet = [1,2,1,2,2,2,1,1,2,1]

	dtcobj = tree.DecisionTreeClassifier();
	dtcobj = dtcobj.fit(BallsFeatures,LabelsSet);

	result = dtcobj.predict([[weight,surface]]);

	val = result[0];

	if val == 1:
			print("Your ball name is: Tennis")
	elif val == 2:
			print("Your ball name is: Cricket");
	else:
			print("Not able to predict");

			
def main():
	
	weight = int(input("Enter ball weight: "));

	surface = int(input("Enter ball Surface: "));

	MLTry(weight, surface);


if __name__ == "__main__":
	main();