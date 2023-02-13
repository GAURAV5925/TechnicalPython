a = 23
b= 56


temp = a
a=b
b=temp

print(a,b)


# without temp

a= a+b
b=a-b
a=a-b
print(a,b)