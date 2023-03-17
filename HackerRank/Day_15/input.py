n = list(map(int,input().split()))
x = n[0] #THIS WILL BE THE VALUE OF X
k = n[1] #THIS IS THE KEY VALUE WE HAVE TO COMPARE

p = input()#THIS WILL TAKE THE EXPRESSION 

if eval(p) == k: #HERE WE ARE SUBSTITUTING THE VALUE OF X AND EVAL
    print("True")
else:
    print("False")
