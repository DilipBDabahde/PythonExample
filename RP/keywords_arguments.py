#keywords aregument


def batches(name, fees):
	print("batch name is: ",name)
	print("fees is: ",fees)


def main():
	batches(name="PPA",fees=8000);
	
	batches(fees = 11000, name='LSP');
	

if __name__ == "__main__":
	main();
