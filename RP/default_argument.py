
def fun(iNo = 10):
	print("val of no: ",iNo)


def main():
	fun();  # 10
	fun(30); # 30

# if we pass val to while calling fun then that val will be shown else default val is used


if __name__ == "__main__":  #control comes first here
	main();
