lower = ""
upper = ""
even = ""
odd = ""

s = sorted(input())

for i in s:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif int(i)%2!=0:
        odd += i
    else:
        even += i
        
        
print(lower + upper + odd + even)
