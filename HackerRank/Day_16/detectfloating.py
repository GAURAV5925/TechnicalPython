import re

pattern = r'^[+-]?[0-9]*\.[0-9]+$'
'''
Here the [+-] --> means staring can be + or - sign
then it can start with multiple digits (its optional)
"*" -- > means multiple times can be repeated
then "." --> this is compuslory
then "+" --> also means can repeat multiple times
then "$" --> means this can be ending
'''

for i in range(int(input())):
    num = input()
    if re.match(pattern,num):
        print("True")
    else:
        print("False")
