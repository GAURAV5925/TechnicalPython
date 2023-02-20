'''class Example:
    value1 = 10
    value2 = 100

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        

    def random(self,a,b):
        self.a=a
        self.b=b
        print("Addition of the Static Variable",self.value1+self.value2)
        print("My Name is",self.name,"and my roll no is",self.rno)
        print("The addition of the two number are ", a+b)


obj = Example("Gaurav",47)
obj.random(10,20)
'''

## 4 Pillars of 

#Inheritnace - Single

'''
class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name = f_name
        self.department= department
        self.f_id = f_id

    def print_info(self):
        print("Faculty information= ",self.f_name,self.department,self.f_id)

class Cse(Faculty):
    pass
obj = Cse("Gaurav","ENTC",1001)
obj.print_info()
'''

#Single Inheritance 

'''
class College:
    def college_name(self):
        print("DYPIT")

class Student(College):
    def student_info(self):
        print("Name : Gaurav")
        print("Branch: Entc")
        print("Roll No. 01")

obj = Student()
obj.college_name()
obj.student_info()
obj.student()
'''


# Multiple Inheritance

'''
class SubjMarks:
    math = int(input("Enter paper marks of math"))
    DC = int(input("Enter paper marks of DC"))
    c = int(input("Enter the c language marks"))
    English = int(input("Enter the marks of the ENglish"))

class PractMarks:
    cpract = int(input("Enter the practicals marks in c language"))


class Result(SubjMarks,PractMarks):
    def total(self):
        if self.math>=40 and self.DC>=40 and self.c>=40 and self.English>=40 and self.cpract>=20:
            print("You have Passes the Exam")
        else:
            print("Sorry You failed the exam")

obj = Result()
obj.total()
'''


#Polymorphism Example

'''
class Principal:
    def role(self):
        print("I am managing the college")


class Dean:
    def role(self):
        print("Dean I am Decision making of the college")
    

class Hod:
    def role(self):
        print("Hod=I am managing the teacher and the student")


class Faculty:
    def responsibility(self):
        print("Faculty - I do nothing")


def func(obj):
    obj.role()
campus=[Principal(),Dean(),Hod()]
for obj in campus:
    func(obj)
'''

# In python method overloading is not possible
# If we are trying to declare multiple with same name and diff. number of arguments then Python will always consd. only last method

# --------METHOD OVERLOADING--------

'''
class Arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):   #Here most recent overloaded method will be considered
        print(a+b+c)

obj = Arithmetic()
obj.add(10)          #This method call will cause the error 
obj.add(10,20)
obj.add(1,2,3)       #If we call this method directly then no error will occur
'''


#Construtor overloading


class Arithematic:
    def __init__(self):
        print("There is no argument")
    def __init__(self,a):
        print("passing one argument")
    def __init__(self,a,b):                       # As in method overloading this will also conder the most recent method
        print("Passing two arguments")

obj = Arithematic()                  #This line will cause the error as the most recent method has the 2 arguments
obj = Arithematic(10)
obj = Arithematic(2,2)                #This will implement the code

'''
# Method overriding concept


class Father:
    def bike(self):
        print("BMW")

    def laptop(self):
        print("Normal Laptop")


class Gaurav(Father):
    def laptop(self):
        print("Not acceptable")
        print("Laptop shoud be Gaming")

obj = Gaurav()
obj.bike()
obj.laptop()


#Constructing Overriding

class Father:
    def __init__(self):
        print("Father timing for breakfast 8.00 am")

class Child(Father):
    def __init__(self):
        print("Child i will not be able to Breakfast at 8.00 am")

obj = Child()

class Father:
    def __init__(self):
        print("Father is at breakfast at 8.00 clock")

class Child(Father):
    def __init__(self):
        print("Child will not be at breakfast at 8.00 clock")
        super().__init__()

obj = Child()

'''





'''
Homeowork - Day 7 (20/02)

Area of triangle
SWapping Of Two var
Leap Year Checking
Calculator with simple arithmetic operation
celcius to faranheit

'''



