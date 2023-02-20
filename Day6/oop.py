### Type of Variable :
# LOcal Variable : It is the varable which is declared inside a method Note : We can also access the variable using the objects
# Static Variable : It is the variable which is declared insode the class and outside of the method
# Instance variable : It is the variable which Defer with the objects

# For Eg--> def random:
#               self.localvariable = instance variable

#  In the construtor we can assign  directly the values and can call it without using the obj it will be called when we create a object 






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

'''
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
'''


#Example 4

class College:
    collegename="DYPIT"   #This is a static variable as it is outside the method and inside the class 

    def __init__(self):
        self.studentname= "Gaurav"            #Here studentname is a local vairable

principal = College()
teacher = College()
accountant = College()

principal.studentname="Pratik"

print("Principal",principal.collegename,"...",principal.studentname)
print("Teacher", teacher.collegename,"...",teacher.studentname)
print("accountant", accountant.collegename,"...",accountant.studentname)

College.collegename="HBO" #using the classname we can access the static VARIABLE
principal.studentname="Gaurav Jha"

print("principal =", principal.collegename,"|",principal.studentname)
print("teacher ",teacher.collegename,"|",teacher.studentname)
print("accountant",accountant.collegename,"|",accountant.studentname)



