#self parameter is a reference to the current instance of the class
#it is used to access the properties and methods that belongs to the class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello my name is",self.name)


p1=person('venkat',23)
p1.greet()
#note: self parameter must be the first parameter of any method in the class
#without self we not know which object's property we want to access
#every method must consists of atleast self parameter 
p2=person('nobi',24)
p2.greet()
'''self is no needed to always name it has self we can use any word
instead of self 'but we have to keep it as first parameter' of the any method'''
class person:
    def __init__(ven,name,age):
        ven.name=name
        ven.age=age

    def greet(ven):
        print("my name is",ven.name)

p=person('nobi',22)
p.greet()
'''Note: While you can use a different name, it is strongly recommended to
use self as it is the convention in Python and makes your
code more readable to others.'''
#accessing multiple properties useing self
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
         print(self.brand,self.model,self.year)

car1=car('bmw','new_ai',2026)
car1.display_info()


#calling methods with self
#call on emethod from another method useing self
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"hello {self.name}"
    def welcome(self):
        message=self.greet() #here we called self method using self and asigned to message
        print(message+"welcome to warangal back")

p1=person('venkat')
p1.welcome()
        
