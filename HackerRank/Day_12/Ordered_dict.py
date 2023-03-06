from collections import OrderedDict



od = OrderedDict()

for i in range(int(input())):
    str = input().split()
    k = " ".join(str[:-1]) #Here except the last element from the string we will take all and join it 
    v = int(str[-1]) #Here we are taking the last element which will be converrted into a int
    
    if k in od: #Checking weather that element is present or not
        od[k] = od[k] + v #we will just add the value for that key
    else:
        od[k] = v #If element is not present we will just add that key and value with it
        
for k,v in od.items(): #dict_name.items() have the key value pair which will iterate through out the dictionary and we will print it
    print(k,v)
