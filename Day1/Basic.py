import math
#same as include<stdio.h> its a header file

# print("Hello World")

# #Python Data Type Int String Float

# print(2/3)

# print(2//3)

# print(2**3)

# #To get the data type
# x=3
# type(x)

# """For Remainder"""
# print(17%3)

# #For Last Digit
# print(1234%10)


## 3 PART OF PROGRAM INPUT, OUTPUT & PROCESS 


#For Volume of Sphere
#After adding int Type Casting will occur before it was string type
rad = int(input("Radius:"))

#pi= 3.14

#If rad**3 It will throw an error TypeError because rad was of string type after adding int typecasting will occur and error will be removed 
vol = 4/3*math.pi* rad**3
#print("The Volume of sphere with the", rad, "is" , round(vol,3))

#Alternate Method
#print("The Volume of sphere with the" + str(rad) + "is" + str(round(vol,3)))
print("The Volume of sphere with the with the radius {} is {}".format(rad,round(vol,1)))




