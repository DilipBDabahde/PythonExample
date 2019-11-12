'''
Accept length and wide of rectangle and calculate its area
(Length * Width).
Input : 4.2    8.9
Output : 37.38
'''

def AreaRect(length, width):	
		return length*width;


def main():
	flength = float(input("Enter length: "));
	fwidth	= float(input("Enter width: "));
	fres = AreaRect(flength,fwidth);
	print("Area Rectangular is: ",fres);


if __name__ =="__main__":
	main();
