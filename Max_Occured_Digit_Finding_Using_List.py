'''
accept num from user and find max time occured digit from that number
input: 32454443
output: 4
'''



def Max_Time_Occured_Digit(iNo):
	list1=[];
	list2=[0,0,0,0,0,0,0,0,0,0];
	
	while(iNo != 0):
		digit=iNo%10;
		list1.append(digit);
		iNo = int(iNo/10);
	

	for i in range(len(list1)):
		if list1[i] == 0:
			list2[0] += list2[0]+1;
		elif list1[i] == 1:
			list2[1] += list2[1]+1;
		elif list1[i] == 2:
			list2[2] += list2[2]+2;
		elif list1[i] == 3:
			list2[3] += list2[3]+1;
		elif list1[i] == 4:
			list2[4] += list2[4]+1;
		elif list1[i] == 5:
			list2[5] += list2[5]+1;
		elif list1[i] == 6:
			list2[6] += list2[6]+1;
		elif list1[i] == 7:
			list2[7] += list2[7]+1;
		elif list1[i] == 8:
			list2[8] += list2[8]+1;
		elif list1[i] == 9:
			list2[9] += list2[9]+1;
			
	imax = list2[0];
	j=0;
	for i in range(len(list2)):
		if(list2[i] > imax):
			imax = list2[i];
			j=i;
	
	return j;gi
	
	

def main():
	
	val = int(input("Enter a Num:"));
	res =Max_Time_Occured_Digit(val);
	print("Maxtime occured digit is: ",res);


if __name__ == '__main__':
	main();
