class myclass2:
    def __init__(self,name,age):
        self.name=name
        self.age=age


#__init__() used to assign the parameters or assign values and it called automatically when the object is created
p1=myclass2("venkat",23)
print(p1.name)
print(p1.age)
'''Note: The __init__() method is called automatically every time
the class is being used to create a new object.'''
#default values in __init__()
class person:
    def __init__(self,name,age=21): #giving age as default value is 21
        self.name=name
        self.age=age


p1=person('venkat')#here we not mentioned age so it takes default value 21
p2=person('nobi',23)#here we mentioned age so it takes the mentioned value only 
print(p1.name,p1.age) 
print(p2.name,p2.age)
#multiple parameters : we can pass any number of parameters to the __init__()
class person_details:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country

p1=person_details('venkat',23,'warangal','india')
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#example
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(f'{self.name} says woof!')


d1=Dog('buddy',23)
d1.bark()
