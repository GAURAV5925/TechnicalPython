from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

c = list(combinations(l,k)) #Making the combinations for eg --> (a,a) (a,c) (a,d) and so on add making a list type of it

res = [i for i in c if 'a' in i] #Here we are making a list in which the char a is present for eg i = (a,a) in which i is present then it will be aded into the list

print(round(len(res)/len(c),3)) #Rounding of the value till three digits and we are taking the total element in original combinations to the req res which will be out probablity
