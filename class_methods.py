'''class methods are the functions that belongs to class and
they define the behaviour of the objects created from the class'''
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello my name is ",self.name)


p1=person('venkat')
p1.greet()
#note : self is the first parameter for all methods
#methods with parameters
'''methods accept parameters just like functions'''
class calculator:
    def add(self,a,b): #giving parameters a,b to the add method
        return a+b
    def mul(self,a,b): #giving parameters a,b to the mul method
        return a*b

cal=calculator()
print(cal.add(2,4))#here passing values to the method
print(cal.mul(7,8))#here passing values to the method

#methods accessing properties
'''methods can access and modify properties useing 'self' '''
class person:
     def __init__(self,name,age):
        self.name=name
        self.age=age
     def get_info(self):
        return f'{self.name} is {self.age} years old'


p1=person('venkat',23)
print(p1.get_info())

#methods modifying properties
'''methods modify the properties of an object'''
#cahnging the property value with example
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def celebrate_birthday(self):
        self.age+=1
        print(f'happy birthday !you age now {self.age}')

p1=person('venkat',22)
p1.celebrate_birthday()
p1.celebrate_birthday()


'''__str__() #it is a special method that
controls what is returned when the object is prined'''
#without __str__()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person('venkat',23)
print(p)

#with __str__()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name} ({self.age})'

p=person('venkat',23)
print(p)

#multiple methods
'''a class has multiple methods that work to gether'''
class playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)  #append() to add items
        print(f'added : {song}')
    def remove_song(self,song):
        self.songs.remove(song) #remove() to remove items
        print(f'removed : {song}')
    def show_songs(self):
        print(f'playlist {self.name}')
        for s in self.songs:
            print(f'-{s}')


p=playlist('fav')
p.add_song('nana nuvu naa pranam')
p.add_song('amma amma naa venala')
p.add_song('malli rava erojuki')
p.show_songs()

#delete a method
del playlist.remove_song '''del keyword wih classname.methodname'''
p.remove_song() #shows error because its deleted
