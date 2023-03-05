#Regex is nothing but we find some pattern in a certain docs or text files

import re

for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
