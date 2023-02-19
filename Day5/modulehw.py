# Q1. To Find Prime Number
# All the odd number are prime number except for 2
# Note : Negative number are not prime or composite

'''
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

'''

# Q2. To find Odd Number
# Note : Zero is also a even Number
# Note : Negative number can be Odd or Even

'''
def odd():
    a = int(input("Please Enter a Value: "))

    if a%2==0:      
        print("Given number is a Even number ")
    else:
        print("Given number is a odd number ")

odd()
'''

# Q4. Given number are vowel or not

'''
def vowel(name):
    j = 0

    for i in name:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            j=j+1
            
    print(" No of Vowels Present are",j)
        
        
name = str(input("Enter the string: "))
new_name = name.lower()
vowel(new_name)
'''


# Q5. Palindrome of an integer

def palindrome(value):

    for i in range(0,int(len(value)/2)):
        if value[i] != value[len(value)-1-i]:
         print("Not a Palindrome")
         break
        
        else:
            print("Palindrome")


value = 121
new_value = str(value)

palindrome(new_value)
    


