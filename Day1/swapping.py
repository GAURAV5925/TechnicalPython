a = 23
b= 56


temp = a
a=b
b=temp

print(a,b)


# without using temp variable

a= a+b
b=a-b
a=a-b
print(a,b)

#Third wasy of swapping

a = 10
b = 30

print(a,b)
[a,b] = [b,a] #using list/tupple we can also swap

print(a,b)
