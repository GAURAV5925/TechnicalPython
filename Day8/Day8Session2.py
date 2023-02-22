# Alogorithm : For the three digit reversal

'''num = int(input("Please enter the number"))

a = num % 10
num = num//10
b = num%10
num = num //10
c = num % 10
rev = (a*100)+(b*10)+(c*1)

print(rev)'''

# Linear Search

'''
def linear(lis,n,k):
    flag = True

    for i in range(n):
        if lis[i] == k:
            flag = False

    if flag == False:
        print(f"Element is at {i}")
    else:
        print("Element not found")
    


n = int(input("Please enter the size of the list"))

lis=[]
for i in range(n):
    element = int(input(f"enter the {i} element"))
    lis.append(element)

print(lis)

linear(lis,n,20)
'''


# ------B I N A R Y   S E A R C H --------


# In Binary Search we need the sorted array
# First we calculate the middle element
# Then we check weather the middle element is equal ,less than or greater than the middle element
# 


lis = [12,13,14,15,20]


def bin(lis,size,target):
    start = 0
    end = size-1

    while(start<=end):

        mid = start + (end-start)//2

        if(lis[mid]==target):
            return mid
        
        elif(lis[mid]<target):
            start= mid + 1

        else:
            end = mid-1

    return -1
    
print(bin(lis,5,14))
