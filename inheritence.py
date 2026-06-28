'''inheritance is used to inherite all the methods and
properties from one class to another class
1.parent class:also know as base class it will be inherited to the child class
2.child class :also called derived class which inherite properties from parent class'''
#creating parent claas
'''Any class can be a parent class, so the syntax is the same as creating any other class'''
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname ,self.lname)

p=person('venkat','balusukuri')
p.printname()
'''To create a class that inherits the functionality from another class,
send the parent class as a parameter when creating the child class:'''
class student(person): #creating a child and parent is person
    pass
'''Note: Use the pass keyword when you do not want to
add any other properties or methods to the class.'''
#Now the Student class has the same properties and methods as the Person class.
x=student('nobi','nobitha')
x.printname()
#adding __init__() to child
class student(person):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
'''When you add the __init__() function,the child class will
no longer inherit the parent's __init__() function.'''
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function
'''To keep the inheritance of
the parent's __init__() function, add a call to the parent's __init__() function'''
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
'''Now we have successfully added the __init__() function, and kept the inheritance of the parent class,
and we are ready to add functionality in the __init__() function.'''
#super() which help child class to inhertite properties of parent class
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname) #no need to mention parent name it automatically inheritate
        
#adding properties
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname ,self.lname)

class student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year


x=student('venkat','balusukuri',2027)
print(x.graduationyear)
#adding method to child class
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname ,self.lname)

class student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

    def welcome(Self):
        print(f'welcome {Self.fname} {Self.lname} to the class of {Self.graduationyear}')

x=student('venkat','balusukuri',2027)
x.welcome()
'''note :If you add a method in the child class with the same name as a function in the parent class,
the inheritance of the parent method will be overridden.

 

        
