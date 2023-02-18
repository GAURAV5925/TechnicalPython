## EXAMPLE 1

'''
class Student:
    def __init__(self):   #This is a Constructor which have a default parameter as self
        self.s_name = input("Enter your name")  
        self.s_rollno = 101   #Instance Variable aka Data Member

    def getdata(self):
        self.s_mb = 280505060

obj = Student()
obj.getdata()
obj.s_branch = "ENTC"  #Here we are declaring this value outside the class using the object
del obj.s_rollno
print(obj.s_name)
print(obj.__dict__)
'''


## Example 2

'''
class Student:
    def __init__(self):
        self.s_name = "Gaurav"
        self.l_name = "Jha"
        self.s_rollno = 101
        self.s_branch = "ENTC"
        self.s_mb = 1254565


obj = Student()
print(obj.__dict__)
'''

# Example 3

class Hod:
    def __init__(self):
        self.name="Gaurav"
        self.age=21
        self.rollno=47

    def info(self):
        print("My Name is:", self.name)
        print("My Age is: ", self.age)
        print("My emp id:", self.rollno)

obj = Hod()
obj.info()


