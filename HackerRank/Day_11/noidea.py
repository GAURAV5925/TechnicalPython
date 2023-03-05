n,m = map(int,input().split())
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(sum((i in A) -(i in B) for i in arr))

# Here the basic idea is that if we get the element which is present in the A list we will add +1
# If we get any element from list B we subtract -1
# Here in the same sum function we have implemented the for loop
