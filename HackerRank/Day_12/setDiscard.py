n = int(input())
s = set(map(int, input().split()))
C = int(input()) #For the number of commands

for _ in range(C):
    
    N = input().split() #Here we will take the command in list type
    
    if N[0] == "remove": #Here on the 0th index the command will be present
        e = int(N[1])  #Here on the 1st index the element to be removed will be present
        s.remove(e)
        
    elif N[0]== "discard":
        e = int(N[1])
        s.discard(e)
        
    else:
        s.pop()

print(sum(s)) #Printing the sum of the set
        
