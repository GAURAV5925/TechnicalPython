n,m = map(int,input().split())# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = ".|."
s2 = "WELCOME"

for i in range(n//2):
    print((s1 * (( i * 2) + 1)).center(m,'-'))
    
print(s2.center(m,'-'))

for i in range(n//2-1,-1,-1):   #Here we have to iterate reverse order hence [Start = ending element,end = ending - 1 as the last element is exclusive, -1 for reversing]
    print((s1*((i*2)+1)).center(m,'-'))
    
