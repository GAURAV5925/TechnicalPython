# Typecasting of Another data type into int type

print(int("4"))
print(int(True))
print(int(False))
# print(int(1+3j))     #error
# print(int("Gaurav")) #error
# print(int("4.22"))   #error at a time only one conversion is possible

# Typecasting of another data type in float type

print(float(4))
print(float(3.12))
print(float(True))
print(float(False))
# print(float(3 + 4j))     # not possible for complex no's
# print(float("Gaurav"))   # not possible for String to convert into float values

# Typecasting of another data type in string type

print(str("Gaurav"))
print(str(123))
print(str(4.22))
print(str(True))
print(str(False))
print(str(3+2j))
print(str(""))

# Typecasting of another data type in complex type

print(complex(4))
print(complex(4,5))
print(complex(True))
print(complex(False))
print(complex(True, False))
print(complex(False, True))
print(complex(4.22,3.12))
print(complex(1 + 2j))      # this will print the same value
# print(complex("gaurav")) error

# Typecasting of another data type in boolean type every value is true only null values are false

print(bool(True))
print(bool(False))
print(bool("Gaurav"))
print(bool(""))
print(bool(0))
print(bool(1))
print(bool(3+2j))
