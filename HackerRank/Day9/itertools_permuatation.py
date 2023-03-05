from itertools import permutations

n = input().split()

char = sorted(n[0]) #Here we are sorting the letter in ascending order 
size = int(n[1])

print(*list(map("".join,permutations(char,size))),sep="\n")  #Permutation method will help in getting the diff way of combination of that two letter 
# sep will separte the result to new line
