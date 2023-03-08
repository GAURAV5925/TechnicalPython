from itertools import combinations

n = input().split()

string = sorted(n[0])
num = int(n[1])

for i in range(1,num+1):
    x = list(combinations(string,i)) #Here we are using i for the subtring len = 1,2...n
    for val in x:
        print("".join(val)) #Here we are joining the val which are present in the list


