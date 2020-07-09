#variable number of arguments

def add(*no):
	ans = 0;
	
	for i in no:
		ans = ans + i;
	
	return ans;

def std_info(**data):
	print(data);
	for i,j in data.items():
		print(i,j);
		
		
def main():
	
	print("Demo of variable num of arguments");
	
	ret = add(10,20,30);
	print("Addition is: ",ret);
	
	ret = add(10,20,30,40,50,60);
	print("Addition is: ",ret);
	
	ret = add(10,21);
	print("Addition is: ",ret);

	print("Demonstration of Keyword Variable number of Arguments")
	std_info(age=28, name = 'Dilip Babulal Dabhade', address = 'ShektaGaon', Mob_num= 7972245697);
		


if __name__ == "__main__":
	main();
