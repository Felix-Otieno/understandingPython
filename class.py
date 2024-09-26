# A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python, a class is created by the keyword class.

class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

# In Python, __init__ is a special method which is automatically called when an object of that Class is created. We use the __init__ method to initialize the attributes of an object.

class Car:
    def __init__(self, brand, model, year):
        # These are object attributes initialized when an object is created
        self.brand = brand
        self.model = model
        self.year = year

# Creating an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the attributes
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)   # Output: 2020

# Methods in objects are functions that belong to the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is " + self.name) 
person1 = Person("Maxwell", 25)
person1.myFunc()        

# The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.

class Human:
    def __init__(personMan, name, gender, age):
        personMan.name = name
        personMan.gender = gender
        personMan.age = age
    def  myInfo(abc):
          print("Hello my name is " + abc.name + " and I am a " + abc.gender +  ". I am " + str(abc.age) + " years old.")    
obj = Human("Mugabe Maurice", "boy", 12) 
obj.myInfo()        
        