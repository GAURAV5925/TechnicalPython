#Variable lenght function

def varlen(*name):
    print(name)

varlen("Gaurav","Jha","Something")  #Here even if the no's of parameters are not fixed we can assign as much as values



#Generator FUnction uses "yield" keyword 
# Improves memory utilization and performance

#Lambda functions
# Syntax -->   lambda arguments : expression


x = lambda a : a +10
print(x(5))


x= lambda a,b : a*b
print(x(10,5))



def myfunc(n):
    return lambda a,b : (a+b) *n  

mydouble = myfunc(2)  #First we will assign the value of n=2

print(mydouble(11,12)) #Then we will give the  value of lambda method


# Generator Function

def simpleGenerator():
    yield "Gaurav"
    yield 2
    yield 3.14

for value in simpleGenerator():
    print(value)


# Fibonacci Series


def fib(limit):

    a,b = 0,1
    while a<limit:
        yield a
        a,b = b,a+b

x = fib(5)

print(next(x))
print(next(x))
print(next(x))



#Exception Handling 


a= int(input("Enter your first value"))
b= int(input("Enter your seconfd number"))

try:
    print(a/b)
except:
    print("Division by zero Exception")



# Exp 2 for Exception 


try:
    print(2/0)

except ZeroDivisionError as message:
    print("The description is ", message)


#Exp 3

a= int(input("Enter first no"))
b=int(input("Enter second no"))

try:
    print(a/b)
except:
    print(a/(b+1))

# Exp 4

try:
    a=int(input("Enter first integer no"))
    b=int(input("Enter your second integer"))
    print(a/b)
except ZeroDivisionError as message:
    print("plz enter the number that is non-zero ")
except ValueError as message:
    print("Error only integer no",message)


# Example 5


try:
    a=int(input("Enter first integer no"))
    b=int(input("Enter your second integer"))
    print(a/b)
except ZeroDivisionError as message:
    print("plz enter the number that is non-zero ")
finally:
    print("Error only integer no")


# Example 6 (Nested try except block)

try:
    a= int(input("Enter first number"))
    b=int(input("Enter your second number"))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)

except ValueError as msg:
    print(msg)


# User DEfined exception by raise keyword







