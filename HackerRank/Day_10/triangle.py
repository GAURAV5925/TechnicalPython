import math

AB = int(input())
BC = int(input())

print(round(math.degrees(math.atan(AB/BC))),chr(176),sep="")

# As the BM = 1/2(AC) 
# BM = 1/2(MA+MC)   ---> We also know that MA = MC
# Hence BM = 1/2(2MC) ---> BM = MC
# Hence BMC will be a isoceles triangle
# Whose angle BMC = MCB
# We take tan(theta) = AB / BC
# After taking theta = tan-1(AB/BC)
# We will get the same angle for the MBC
#Here in the question we get the isoceles triangle
# using math module we calculate the inverse of the tan
# Here we are typecasting the 176 which in ASCII code is Degree symbol
