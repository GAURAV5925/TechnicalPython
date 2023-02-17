'''
#First Way of importing module

import session1

session1.square(4)
session1.welcome()
session1.login()


#Second way of importing module

import session1 as s

s.square(5)
print(s.pi)
s.welcome()
s.login()



#Third way of importing module

from session1 import square,welcome,login

square(15)
welcome()
login()


#Fourth way of importing module

from session1 import *

square(15)
print(pi)
welcome()
login()
'''



## My method implementation 



#First way of implementation


import math_module

math_module.search_letter("Gaurav")

name="MADAM"
name=name.lower()
math_module.palindrome(name)

math_module.bigthree()

result = math_module.arith(10,5,2)
print(result)


#Second way of Implementation


import math_module as math

math.search_letter("Gaurav")

name="MADAM"
name=name.lower()
math.palindrome(name)

math.bigthree()

result = math.arith(10,5,2)
print(result)


#Third way of Implementation


from math_module import search_letter,palindrome,bigthree,arith

search_letter("Gaurav")

name="MADAM"
name=name.lower()
palindrome(name)

bigthree()

result = arith(10,5,2)
print(result)


#Fourth way of Implementation


from math_module import *

search_letter("Gaurav")

name="MADAM"
name=name.lower()
palindrome(name)

bigthree()

result = arith(10,5,2)
print(result)




