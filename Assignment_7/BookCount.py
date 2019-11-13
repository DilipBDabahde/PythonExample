'''
1.Write a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name ,Author.
That class contains one class variable as NoOfBooks which is initialise to 0.
There is one instance methods of class as Display which displays name , Author and number of
books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.

After creating the class create the two objects of BookStore class as
'''


NoOfBook = 0;
class BookStore:
		
	
	def __init__(self,naav,lekhak):
		global NoOfBook;
		NoOfBook = NoOfBook + 1;
		self.BName=naav;
		self.Author=lekhak;
		
	def Display(self):
		global NoOfBook;
		print("BookName  : ",self.BName);
		print("AuthorName: ",self.Author);
		print("Total Books are: ",NoOfBook);
		print("----------------------------");
	
	
obj1 = BookStore("C Programming","K&R");
obj1.Display();

obj2 = BookStore("Linux system programming","Robert Love");	
obj2.Display();

obj3= BookStore("C++","Bjarne Stroustrup");
obj3.Display();
	

