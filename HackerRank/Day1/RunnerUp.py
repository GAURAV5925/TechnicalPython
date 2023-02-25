'''
Here the concept of the List is Learned
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) # .split() function will split the string into a list type
    

    print(sorted(set(arr))[-2])  #Here we first converting the list into a set then we are taking the second highest value using the negative indexing
