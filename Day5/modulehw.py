# Q1. To Find Prime Number
# All the odd number are prime number except for 2
# Note : Negative number are not prime or composite

'''
def prime():
    a = int(input("Please Enter a Value: "))

    if a<=0:    
        print("Please enter a valid number ")
    elif a%2==0 or a==2:   
        print("Given number is a Composite number ")
    else:
        print("Given number is a prime number ")

prime()
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
    


