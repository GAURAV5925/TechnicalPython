## Q1. Addition of two values

'''def add(value1,value2):
    print("Addition of two number is: ",value1+value2)

a = int(input("Enter your 1st value"))
b = int(input("Enter your 2nd value"))

add(a,b)'''


## Q2. Max of two values

'''
def max_two(a,b):
    if a>b:
        print("A is largest")
    elif a==b:
        print("A is equal to B")
    else:
        print("B is largest")

a = int(input("Enter the value of A "))
b = int(input("Enter the value of B "))

max_two(a,b)
'''


## Q3. Program for Simple Interest

'''def sim_int(p,r,t):
    si=(p*r*t)/100
    print("Simple interest is",si)

p = float(input("Enter the principal amount"))
r = float(input("Enter the rate"))
t = float(input("Enter the duration"))

sim_int(p,r,t)'''

## Q4. Program for Compound Interest

'''def ci(p,r,t):
    ci = p*(1+(r/100))**t - p
    print("Your Compund Interest is ", ci)

p=float(input("Enter your principal amount: "))
r=float(input("Enter your rate: "))
t=float(input("Enter your Time: "))
ci(p,r,t)
'''

## Q5. Area of circle


import math

def area_circle(radius):
    area = math.pi * radius * radius
    return area

r = float(input("Enter the value of circle "))

result = area_circle(r)
print("Area of circle is", result)

