'''class properties are the variables that belongs to class,
they store data for each object created from the class'''
class person:
    def __init__(self,name,age):
        self.name=name #here name ,age are the properties
        self.age=age
#accessing the properties
p1=person("venkat",23)
print(p1.name) #accessing th propertie called name
print(p1.age)  #accessing th propertie called age
#modifying the properties
p1.name='nobitha'#we can modify by assigning new vlue to the propertie of that particular object 
print(p1.name)
#deleting the property
'''we can delete property by useing "del" keyword'''
del p1.age #age is deleted from p1 object but not completely for class
print(p1.name)#shows output because it present
   ##print(p1.age)#shows error because the propertie is deleted and now its not present in the p1 object
#the propertied defined inside the __init__() are object or instance properties
#the propertied defined outside the __init__() are class properties
class person:
    species='human' #class properties
    def __init__(self,name):
        self.name=name # instance properties (instance:unique occurence of the class)

p1=person("venkat")
p2=person("nobitha")
print(p1.species)
print(p2.species)
#modifying class properties
'''note: modifying class properties ,it affects all objects'''
class person:
    lastname=' '
    def __init__(self,name):
        self.name=name

p1=person('venkat') 
p2=person('nobitha')
print(p1.lastname)
print(p2.lastname)
person.lastname='balusukuri' 
print(p1.lastname)
print(p2.lastname)

#adding new properies
#we can add new properties to an object
class person:
    def __init__(self,name):
        self.name=name

p1=person('venkat')
p1.age=24
p1.city='warangal'
print(p1.name)
print(p1.age)
print(p1.city)
'''Note: Adding properties this way only adds
them to that specific object, not to all objects of the class.'''
        
