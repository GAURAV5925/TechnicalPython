def prime(value):
    flag = True     #Flag can be any assigned value and instead of flag we can use any name for eg. --> isPrime = True
    for i in range(2,value//2):   #No need to iterate for the complete n value we can just iterate till the n//2 value Here "//" will conver the float value into integer
        if value%i==0:
            flag=False   #If the condition satisified flag will become true and Break keyword will stop the execution of the loop
            break
    
    if flag==False:           #If we will use directly IF-ELSE Statement in the for loop it will not be able to catch the exception such as 15, 21 and so on
        print("Not a Prime Number")
    else:
        print("Prime Number")

num = int(input("Enter a Number"))
prime(num)
