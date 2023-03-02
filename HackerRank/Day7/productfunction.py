from itertools import product


#First we will take imput in split manner
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(*list(product(a,b)))

#product() function works same as mulitplying one equation with other first we mulitply 1st term with all other term of the another equation

#Here * will make the list iterable object meaning we will not have to create a for loop for i to print
