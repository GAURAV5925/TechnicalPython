# Local & Global Variable
# Modules --> Decreases the line of code
# Function is reusable in that file only
# Module can be used in another file also
# module collection of function
# SYNTAX module_name.function_name(paraameters)
# Using module we can also acess the member value
# fabs give absolute value --> will return only postive calue even for the negative no's
# random default range is 0-1
# radint(starting,end)  --> Integer Random value
# uniform(start,end)   --> Float Random value
# name is a main function if don't immport it will be main function but when we import it will not be   main function
# package is collection of module in single mean package

# In python method overloading is not allowed




#method given by Sir

'''

def welcome():
    print("Hello Python")

def square(value):
    print("Square of The value", value*value)


pi = 3.142

def login():
    while True:
        username = input("Enter username")
        password = input("Enter the password")
        if username==password:
            print("Login Suceesfully")
            break
        else:
            print("Login Failed, Please Retry")
'''

'''
import random

print(random.random())


#This will print the Random Integer 
for i in range(0,10):
    print(random.randint(1,100))



#This will print the random float value
for i in range(0,10):
    print(random.uniform(1,10))



#To Print the random list item
lis = ["gaurav","random","sample"]
for i in lis:
    print(random.choice(lis))   #choice() method from the random module will select any element at random in the sequence data type


'''

from random import *

def lotteryticket():
    value=int(input("Enter your ticket number"))
    lucky = randint(1,10)

    if lucky==value:
        print("Congratulations you won the lottery")
    else:
        print("Better luck next time")

lotteryticket()
