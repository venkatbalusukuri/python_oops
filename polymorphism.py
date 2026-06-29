#polymorphism means one in 'many forms'
'''functional polymorphism where we can see len() can used in
different objects like tuple,list,dixtionary,strings here the len() is
used to find the length'''
#class polymorphism means multiple classes with same method name
#example
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self): #method move()
        print('Drive')

class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self): #method move
        print('snail')

class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self): #method move 
        print('fly')
#here move method is geeting in every class

c=car('bmw',1)
b=boat('savari',91)
p=plane('indigo',98)
for x in(c,b,p):
    x.move() #we executed same methos 3 times


#inheritence class ploymorphism
'''we can use polymorphism for inheritence but the methods of child class
over ride them '''
#example
class vechile:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print('drive')

class car(vechile):
    pass #here the child class inherite the property from parent class directly
class boat(vechile):
    def move(self):#here it override the method and print snail instead of drive in parent class
        print('snail')

class plane(vechile):
    def move(self):#here also it ovveride the method
        print('fly')
#the brand and year properties are inherited from parent class
c=car('bmw',1999) 
b=boat('savari',2000)
p=plane('indigo',2012)
for x in (c,b,p):
    print(x.brand)
    print(x.year)
    x.move()


'''Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes'''


        



