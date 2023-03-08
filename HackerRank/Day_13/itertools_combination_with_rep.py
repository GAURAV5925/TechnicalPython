from itertools import combinations_with_replacement

n = input().split()
string = sorted(n[0]) #Sorting as sorted input will have sorted output
num = int(n[1]) #Typecasting for int type

x = list(combinations_with_replacement(string,num))
#Here we are converting the tuple into a list as the output will be a tuple for the combinations_with_replacement() method

for val in x: #Using this loop we will iterate the list which is x 
    print("".join(val))  #val is the variable we have choosen which will take the value from the list
