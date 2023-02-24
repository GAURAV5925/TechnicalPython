
# -----M E R G E S O R T------
# most optimal sorting algorithm


'''
def mergeSort(arr):

    if len(arr)>1:
            
            mid = len(arr)//2

            L = arr[:mid]

            R = arr[mid:]

            mergeSort(L)

            mergeSort(R)


            i = j = k = 0

            while i<len(L) and j<len(R):
               if L[i] <= R[j]:
                      arr[k] = L[i]
                      i += 1
               else:
                    arr[k] = R[j]
                    j += 1
               k += 1

            while i < len(L):
                 arr[k] = L[i]
                 i += 1
                 k += 1
            
            while j < len(R):
                 arr[k] = R[j]
                 j += 1
                 k += 1

    return arr


arr = []

n = int(input("Please enter the Size of the element"))

for i in range(n):
    element=int(input(f"Enter the {i} element"))
    arr.append(element)

print("Unsorted array",arr)



print("Sorted Array",mergeSort(arr))

'''
    
# S T A C K 


#  Push / Pop OPeration

import time
mystack = []
size = int(input("Enter the size of the stack : "))


for i in range(size):
     a = int(input("push element in stack: "))
     mystack.append(a)
else:
     print("Stack is full")
     print(mystack)

print("pop operation start: ")
for i in range(size):
     time.sleep(3)
     print(mystack.pop(), "pop element from stack")
else:
     print("Stack is empty")
     print(mystack)


# Example 2

stack = []
for top in range(5):
     a = int(input("push a element in stack"))
     stack.append(a)
     top +=1
else:
     print("stack is full")

print("stack = ",stack)
print(" Top = ",top)

for i in range(5):
     print(stack.pop())
     top -=1
else:
     print("stack")
