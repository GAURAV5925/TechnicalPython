import math
import os
import random
import re
import sys





first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
l = list(zip(*matrix))

s = ""

for i in l:
    s = s + "".join(i) #Here we are first zipping means taking the combinations of the element like--> (T,h,i,s,$,#,i) this will use the first column of the array
    
s = re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',s) #Regular expression

print(s)
