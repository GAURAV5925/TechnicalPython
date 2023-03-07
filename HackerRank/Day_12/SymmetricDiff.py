a,b=(int(input()),input().split())
c,d=(int(input()),input().split())

x=set(b)
# Set always have a unique element
y=set(d)

# In the symmetrical Difference --> a element is present in one set but not in both set 

p=y.difference(x) #This will only show the element which are not present in the x but are in y  ---> Here output will be like {'11','12'}
q=x.difference(y) #This will only show the element which are not present in the y but are in x ---> Here output will be like {'5','9'}

r=p.union(q) #Here we will make a union means will take both the elements of p and q  ---> {'11','12','5','9'}

print('\n'.join(sorted(r,key=int)))

# .join() will make the result in one and will break after each space in new line 
# Syntax --> sorted(iterable,key)
# Using key we will convert it into a int as it is in in string format
