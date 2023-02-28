if __name__ == '__main__':
    s = input()
    
    a=b=c=d=e=0  
    for i in s:
        if i.isalnum():
            a+=1
        if i.isalpha():
            b+=1
        if i.isdigit():
            c+=1
        if i.islower():
            d+=1
        if i.isupper():
            e+=1
            
            
    for i in [a,b,c,d,e]:
        if i>0:
            print(True)
        else:
            print(False)
            
            
'''
Here the basic idea is that we will store the value in a,b,c,d,e which is the condition we have to check

After which we will iterate through each element of the list to check if its greater than 1 then we will say that condition is True else False
'''
