from collections import defaultdict

dic = defaultdict(list)
n,m = map(int,input().split()) #Here we are first converting the input in int type then assigning the value to two var 1st input will be for n after space it will go to the m

for i in range(1,n+1):
    a = input()
    dic[a].append(i)  #In the normal case if key is not present we cannot append the item in the dictonary
    
for j in range(m):
    b = input()
    if b in dic:   #Here we are checking weather the imput item is present in our dictionary or not
        print(*dic[b],sep=" ") #Here we will print the list item in different format without comma and bracket and sep function will separte it with a space
    else:
        print(-1)
