'''Abstraction:-
Python doesnt provide bydefault the abstract class
When we have to communicate with 3rd party interface we use python
'''



'''
from abc import ABC, abstractmethod  # Here ABC means --> ABSTRACT BASE CLASS which is a module as we dont have a default Abstract class

class Polygon(ABC):

    #Abstract method
    # We cant create a object of the abstract class due to this we also dont need to declare a constructor
    
    @abstractmethod
    def noofsides(self):
        pass   #Here we use the pass keyword as we just declare the abstract method and it's body should be empty

class Triangle(Polygon):

    # Overiding Abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    
    def noofsides(self):
        print("I Have 5 sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):

    def noofsides(self):
        print("I have 4 sides")

R = Triangle()
R.noofsides()

K= Pentagon()
K.noofsides()

R = Hexagon()
R.noofsides()

K=Quadrilateral()
K.noofsides()

'''

# Example 2

'''
from abc import ABC, abstractmethod

class Programming(ABC): #This class is inheriting the abstract class hence this is the abstract class
    @abstractmethod
    def training(self):
        pass

    def placement(self):
        pass


class Gaurav(Programming):

    def training(self):
        print("C, Java, C++")

    def placement(self):
        print("Java")

class Random(Programming):

    def training(self):
        print("Google, Microsoft, Apple")

    def placement(self):
        print("Microsoft")

class Sample(Programming):
    
    def training(self):
        print("ML, DS, AI")

    def placement(self):
        print("DS")

obj1 = Gaurav()
obj1.training()
obj1.placement()

obj2 = Random()
obj2.training()
obj2.placement()

obj3 = Sample()
obj3.training()
obj3.placement()
'''


## Encapsulation :
# This mechanism is used to protect the data of an object from the objects
# 


# _a (single underscore) --> Protetcted Method
# __a (double underscore) --> Private Method

class Base:
    def __init__(self):
        print("Parent class is called")
        self._a = 2 # This is the protected data member

class Derived(Base):

    def __init__(self):
        Base.__init__(self) #Here we are callng the base class constructor we can also do this using the super keyword
        print("Calling the derived class")
        print(self._a)

obj1 = Derived()
print(obj1._a)

# obj2 = Base()
# print(obj2._a) #This will cause an error as we are calling the protected data member then we have to add a _ before the variable


#  Example 2

class Gaurav:
    def __init__(self):
        print("Parent class cosntructor called")
        self.a = "DYPIT"
        self.__b = "Pimpri"

class Jha(Gaurav):
    def __init__(self):
        Gaurav.__init__(self)
        print("My college name is ", self.a)
        # print("My college is located at", self.__b)   #This line will cause the error as we have mentioned the private data member here even if we use the correct method to call it will not be able to be called in  the another class

obj1 = Jha()



