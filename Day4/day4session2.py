# In this we have learned about the function and implementation of its


#Default Argument

'''
def func(city = "Nagpur"):  #This is the default Argument when no argument are passed
    print("I am from", city)

func("Delhi")
func("Pune")
func()
'''

#Unkown Argument

def some(**name):
    print("My name is ", name["lastname"])

some(lastname="jha", firstname="gaurav")

#Returning mulitple value at a time
'''

def add_product(a,b):
    add=a+b
    product=a*b
    return add,product

x,y = add_product(10,5)
print("Addition of the given term is",x)
print("Product of the given term is",y)
'''

#Passing of List as Argument

'''
def func(name):
    for i in name:
        print(i)

name_of = ["Gaurav","Jha", "Random", "Sample"]
func(name_of)
'''

'''
def func(name):
    j=0
    for i in name:
        if i == "u":
            print("The character 'u' is present at the index",j, "of the value", name)
            break
        j=j+1

name="Gaurav"

new_name = name.lower

func(name)
'''



