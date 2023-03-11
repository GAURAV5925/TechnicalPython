s = input()
count = 1 #Here we are initiating the count as 1 bcos each char will have atleast 1 cosucetive

for i in range(1,len(s)): # We are  starting the loop from 1st element bcos we will check it with the last element
    if s[i] == s[i-1]: #if it will match with last element we will add the count
        count += 1
    else:
        print((count,int(s[i-1])), end=" " ) #If not we will just print it on the console
        count = 1

print((count, int(s[-1]))) #For the last element as we will not be able to iterate till the last element
