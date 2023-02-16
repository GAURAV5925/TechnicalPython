'''def name():
    print("my name is gaurav")
    
name()'''


'''
def login():
    
    while True:
        username = input("Enter username")
        password = input("Enter the password")
        if username==password:
            print("login successfully")
            break
        else:
            print("login failed please enter correct details")
            
login()
'''


'''
import time

def welcome():
    print("Hello Python")
    
print("First time")
time. sleep(2)
welcome ()
print("Second time")
time. sleep(3)
welcome ()
'''

def addition(value):
    print("addition",value+value)

addition(5)


def add(num1, num2):
    return num1 + num2
    
result = add(5, 10)
print("Addition is", result)


def arithmetic (a, b):
    p = a*b
    q = a + b
    r = a-b
    
    return p, q, r
    
result = arithmetic (5, 10)
print (" Following are result",result)


def chk_even_odd(value):
    if(value%2==0):
        print("Even")
    else:
        print("odd")
        
chk_even_odd(5)
chk_even_odd(10)



def info(firstname, lastname):
    print("First Name",firstname)
    print("Last Name", lastname)
    
info("gaurav","jha")
info(firstname="jha",lastname="gaurav")



s= input("Enter the string")
for i in range(0, int(len(s)/2)):
    if s !=s[len(s)-1-i]:
       print("palindrome")
       break
    else:
       print("not palindrome")


