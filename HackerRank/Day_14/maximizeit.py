from itertools import product

n,m = input().split()

n = int(n) #This is the number of list we have to take as input
m = int(m) #Using this we have to perform the modulo operator

lis = list()

for i in range(n):
    l = list(map(int,input().split()))[1:] #Taking the list from the user starting 1st index --> as the {1 or 0th index input will be the size of that list}
    lis.append(l)

res = map(lambda x:sum(i*i for i in x)%m,product(*lis)) 
#In the above line of code we are taking one set of element from the product list then we are taking it square and adding it

print(max(res))
#In this we are just taking the maximum from the list of res
