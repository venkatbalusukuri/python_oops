class myclass: #creating a class named my class
    x=5


a=myclass() #creating a object for class name myclass the object name is a
print(a.x)

del a #to delete the object del keyword and object name
 #print(a.x)
#creating multiple objects
obj1=myclass()
obj2=myclass()
obj3=myclass()
print(obj1.x)
print(obj2.x)
print(obj3.x)
#note : each object is independent and has its own copy of the class properties
#pass stmt :we use pass stmt to avoid errors when we want to create a class with no content
class myclass1:
    pass
