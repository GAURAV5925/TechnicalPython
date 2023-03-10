# --- INSERTION SORT------


'''
def insertion(arr,n):
    for i in range(1,n):
        j = i-1
        key = arr[i]
        while (j>=0) and (key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key


arr = []

n = int(input("Please enter the size of the array"))

for i in range(n):
    element = int(input(f"Enter the {i} Element"))
    arr.append(element)

print("Your Unsorted element",arr)

selection(arr,n)


print("Your sorted array is",arr)
'''


# ---- S E L E C T I O N   S O R T-------

# In the insertion sort first we take a min index which is the first element of that array
# then we check it with all the other element of the array
# if the condition is satisifed than the choosen element that we were comparing we will change the min_index with it 
# and if not we will just iterate the loop further
# Here we ARRANGE THE SMALLEST ELEMENT AT THE STARTING POSTION THEN WE DO THE SAME FOR THE SECOND SMALLEST ELEMENT

# [30, 10, 12, 8, 15, 1]


def selection(arr,n):
    for i in range(0,n):
        min_index = i

        for j in range(i+1,n):
            if(arr[min_index]>arr[j]):
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]


arr = []

n = int(input("Please enter the SIze of the element"))

for i in range(n):
    element=int(input(f"Enter the {i} element"))
    arr.append(element)

print("Unsorted array",arr)

selection(arr,n)

print("Sorted Array",arr)


# -----M E R G E S O R T------
# most optimal sorting algorithm



