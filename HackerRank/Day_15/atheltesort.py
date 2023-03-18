#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter #using this module we can sort the atribute based on the key



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
row = sorted(arr,key=itemgetter(k))  #using the module we imported and give it the key 

for i in row:
    print(*i)
    
