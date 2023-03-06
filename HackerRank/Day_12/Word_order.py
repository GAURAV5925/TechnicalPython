from collections import Counter

n = int(input())
l = list()

for _ in range(n):
    l.append(input())

x = Counter(l) #In the counter the element will be stored in key value format meaning only unique element will be stored
print(len(x)) #Here we are taking the total no of items
print(*x.values()) #Using the unpack operator we are printing the element in a single line and only the values will be printed by values() method
