import numpy

n = int(input())

lis = list()

for _ in range(n):
    e = list(map(float,input().split()))
    lis.append(e)
    
print(round(numpy.linalg.det(lis),2)) #This code will help in calculating the determinant
