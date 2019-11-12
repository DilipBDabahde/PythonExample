'''
2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea(),
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects.
'''


class Demo:
    PI =3.14;
    
    def __init__(self):    	
        self.Radius=0.0;
        self.Area=0.0;
        self.Circumference=0.0;
        
    def Accept(self):
        self.Radius = float(input("Enter Radius: "));
		
    def CalculateArea(self):
        return  self.PI*self.Radius*self.Radius;
		
    def CalculateCircumference(self):
        return  2 * self.PI * self.Radius;  
    
          
    
    
obj2 = Demo();
obj2.Accept();
print("Area of Cicle is: ",obj2.CalculateArea());
print("Circumference of circle is: ",obj2.CalculateCircumference());




