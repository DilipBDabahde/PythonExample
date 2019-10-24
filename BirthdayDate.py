# use of Dictionries as birthday name and date



def BDay():

	birthday={'Anil':"11 Nov","Appa":"12 Dec","Krushna":"15 Nov","Dilip":"29 Nov"};
	
	while True:
		print("Enter the name: (blank to quite)");
		name = input();
		if name=='':
			break;
		if name in birthday:
			print(birthday[name]+' is the birthday of '+name);
		else:
			print("I do not have birthday info of "+name);
			print("What is their birthday");
			bday = input();
			birthday[name]=bday;
			print("Birthday database is updated");
	
def main():
	BDay();
	
	
if __name__ == "__main__":
	main();
