from collections import deque

n = int(input())
d  = deque()

for i in range(n):
    c = input().split()
    
    if c[0]=='append':
        d.append(int(c[1]))
    elif c[0] == 'appendleft':
        d.appendleft(int(c[1]))
    elif c[0] == 'pop':
        d.pop()
    else:
        d.popleft()
        
print(*d) #Unpack Operator
