n = int(input())
num = input().split()

print(all(int(i)>0 for i in num) and any(j== j[::-1] for j in num))
#iterating through the list and cheking the element first we typecasted the element in int type and then check the conditon 
# in second condition any number in string if palindrome the condtion will be satisified here we are considering it as str
